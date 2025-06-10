# Migrating Your Audio Unit Host to the AUv3 API

**Framework**: Audio Toolbox

Update your Audio Unit (AU) host app to take advantage of the new features and capabilities of AUv3.

#### Overview

The latest Audio Unit standard, AUv3, provides a robust plug-in model built on app extensions. This model provides several benefits to host apps, including greater security and stability, multiple view configurations, and support for shared user presets.

You can adopt the new API while still retaining your ability to host AUv2 audio units. The framework’s bridging layer enables this capability by automatically translating AUv3 calls into their AUv2 equivalents, which means you can use a single API and work with both new and legacy audio units.

![A component diagram that shows the bridging support provided by the framework.](https://docs-assets.developer.apple.com/published/f5490fa2df1cfa8948d30e81b2aaeca6/media-3531569%402x.png)

For a downloadable sample app that uses the core features of the AUv3 API, see [`Incorporating Audio Effects and Instruments`](incorporating-audio-effects-and-instruments.md).

##### Find Audio Units

The AVFoundation framework’s [`AVAudioUnitComponentManager`](https://developer.apple.com/documentation/AVFAudio/AVAudioUnitComponentManager) class provides a convenient way to find audio components registered with the host system. You use it to search for audio units by description, predicate, or test case, and the component manager returns an array of [`AVAudioUnitComponent`](https://developer.apple.com/documentation/AVFAudio/AVAudioUnitComponent) objects matching your search criteria. The following code example shows how to use each approach to find all audio effects available on the system.

```swift
// Access the singleton AVAudioUnitComponentManager instance.
let manager = AVAudioUnitComponentManager.shared()

// Retrieve audio unit components by description.
let description = AudioComponentDescription(componentType: kAudioUnitType_Effect,
                                            componentSubType: 0,
                                            componentManufacturer: 0,
                                            componentFlags: 0,
                                            componentFlagsMask: 0)
let componentsByDesc = manager.components(matching: description)


// Retrieve audio unit components by predicate.
let predicate = NSPredicate(format: "typeName CONTAINS 'Effect'")
let componentsByPredicate = manager.components(matching: predicate)

// Retrieve audio unit components by test.
let componentsByTest = manager.components { component, _ in
    return component.typeName == AVAudioUnitTypeEffect
}
```

##### Instantiate Audio Units

Once you’ve found the list of available audio components, the next step is to instantiate the component you want to use. To instantiate the audio unit, use the [`AVAudioUnit`](https://developer.apple.com/documentation/AVFAudio/AVAudioUnit) class’s [`instantiate(with:options:completionHandler:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioUnit/instantiate(with:options:completionHandler:)) method as shown below.

```swift
func selectAudioUnit(at index: Int) {
    let description = components[index].audioComponentDescription
    
    // Instantiate using AVFoundation's AVAudioUnit class method.
    AVAudioUnit.instantiate(with: description, options: []) { avAudioUnit, error in
        guard error == nil else {
            DispatchQueue.main.async { /* Show error message to user. */ }
            return
        }
        
        // Audio unit successfully instantiated.
        // Connect it to AVAudioEngine to use.
    }
}
```

> ❗ **Important**:  A key difference between the two audio unit API versions is that AUv2 audio units are loaded into the host’s process, whereas AUv3 audio units are loaded out-of-process by default. In macOS only, if supported by the AUv3 audio unit, you can request loading it in-process by passing the [`loadInProcess`](audiocomponentinstantiationoptions/loadinprocess.md) option in the `options` argument. To verify that the audio unit was successfully loaded in-process, query its [`isLoadedInProcess`](auaudiounit/isloadedinprocess.md) property.

##### Interact with an Audio Unit

The way you interact with audio units using the AUv3 API differs from how you do so with the AUv2 API. With AUv2, you used C functions to operate on an audio unit. For example, the following code sets the maximum number of frames to render using the AUv2 API.

```swift
// Get the underlying AudioUnit instance.
let audioUnit = avAudioUnit.audioUnit
var maxFrames = UInt32(4096)

// Set the maximum frames to render.
AudioUnitSetProperty(audioUnit,
                     kAudioUnitProperty_MaximumFramesPerSlice,
                     kAudioUnitScope_Global,
                     0,
                     &maxFrames,
                     UInt32(MemoryLayout<UInt32>.size))
```

In comparison, the AUv3 API provides a more natural interface that enables you to interact directly with the audio unit instance by calling its properties and methods. Using the AUv3 API, you set the maximum number of frames to render as shown below.

```swift
// Get the underlying AUAudioUnit instance.
let audioUnit = avAudioUnit.auAudioUnit
audioUnit.maximumFramesToRender = 4096
```

The following table lists the AUv2 function and its AUv3 method or property equivalent.

| AUv2 API | AUv3 API | Description |
| --- | --- | --- |
| [`AudioUnitInitialize(_:)`](audiounitinitialize(_:).md) | [`allocateRenderResources()`](auaudiounit/allocaterenderresources().md) | Allocates the audio unit’s needed resources. |
| [`AudioUnitUninitialize(_:)`](audiounituninitialize(_:).md) | [`deallocateRenderResources()`](auaudiounit/deallocaterenderresources().md) | Frees the audio unit’s rendering resources. |
| [`AudioUnitRender(_:_:_:_:_:_:)`](audiounitrender(_:_:_:_:_:_:).md) | [`renderBlock`](auaudiounit/renderblock.md) | Renders audio samples in a real-time context. |
| [`AudioUnitReset(_:_:_:)`](audiounitreset(_:_:_:).md) | [`reset()`](auaudiounit/reset().md) | Resets the audio unit’s state. |
| [`AudioUnitScheduleParameters(_:_:_:)`](audiounitscheduleparameters(_:_:_:).md) | [`scheduleParameterBlock`](auaudiounit/scheduleparameterblock.md) | Schedules a change to an audio unit parameter value. |
| [`AudioUnitGetProperty(_:_:_:_:_:_:)`](audiounitgetproperty(_:_:_:_:_:_:).md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`AudioUnitSetProperty(_:_:_:_:_:_:)`](audiounitsetproperty(_:_:_:_:_:_:).md) | `audioUnit.propertyName` | Modifies an audio unit property value. |
| [`AudioUnitGetParameter(_:_:_:_:_:)`](audiounitgetparameter(_:_:_:_:_:).md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`AudioUnitSetParameter(_:_:_:_:_:_:)`](audiounitsetparameter(_:_:_:_:_:_:).md) | [`parameterTree`](auaudiounit/parametertree.md) | Accesses the parameter tree object that’s used to get and set parameter values. |

##### Present the Audio Units User Interface

To present the audio unit’s user interface, call its [`requestViewController(completionHandler:)`](auaudiounit/requestviewcontroller(completionhandler:).md) method. This method asynchronously retrieves the audio unit’s view controller instance and returns it in a callback closure. The callback is invoked on a background thread, so you need to dispatch control back to the main queue before adding the audio unit’s user interface into your app’s view hierarchy.

```swift
audioUnit.requestViewController { viewController in
    DispatchQueue.main.async {
        // Install the view controller's view in your host's user interface.
    }
}
```

## See Also

- [Hosting Audio Unit Extensions Using the AUv2 API](hosting-audio-unit-extensions-using-the-auv2-api.md)
  Update your existing Audio Unit v2 host app to load and use Audio Unit extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/migrating-your-audio-unit-host-to-the-auv3-api)*