# Hosting Audio Unit Extensions Using the AUv2 API

**Framework**: Audio Toolbox

Update your existing Audio Unit v2 host app to load and use Audio Unit extensions.

#### Overview

The latest Audio Unit standard, AUv3, provides a robust plug-in model built on app extensions. This model provides several benefits to host apps, including greater security and stability, multiple view configurations, and support for shared user presets.

With only minor modifications to your existing AUv2 host app, you’re able to load and interact with Audio Unit extensions. The framework provides a bridging layer that automatically translates AUv2 calls into their AUv3 equivalents, and vice versa. This bridging is largely transparent to your app, and you’re only required to make minor changes to how you instantiate components and access their user interfaces.

![A component diagram that shows the bridging support provided by the framework.](https://docs-assets.developer.apple.com/published/905c919679c026e3a9b37e5404a6f49c/media-3526605%402x.png)

> **Note**:  AUv2 is in maintenance mode, and it’s recommended that you adopt the AUv3 API for new development.

 AUv2 is in maintenance mode, and it’s recommended that you adopt the AUv3 API for new development.

##### Asynchronously Instantiate Audio Units

AUv3 extensions that provide a user interface require that you instantiate them asynchronously. Attempting to instantiate them using the synchronous [`AudioComponentInstanceNew(_:_:)`](audiocomponentinstancenew(_:_:).md) function fails. Instead, check for the existence of the [`requiresAsyncInstantiation`](audiocomponentflags/requiresasyncinstantiation.md) component flag. If present, asynchronously instantiate the component using the new [`AudioComponentInstantiate(_:_:_:)`](audiocomponentinstantiate(_:_:_:).md) function, as shown in the following code example.

```objc
AudioComponent component = ...
AudioComponentDescription componentDesc;

// Get the component description.
AudioComponentGetDescription(component, &componentDesc);

// Determine if async loading is required.
bool requiresAsync = (componentDesc.componentFlags &
                      kAudioComponentFlag_RequiresAsyncInstantiation) > 0;

if (requiresAsync) {
    // Asynchronous Path
    AudioComponentInstantiate(component,
                              kAudioComponentInstantiation_LoadOutOfProcess,
                              ^(AudioComponentInstance audioUnit, OSStatus error) {
        // Initialize AudioUnit instance.
    });
} else {
    // Synchronous Path
    AudioComponentInstance audioUnit;
    if (AudioComponentInstanceNew(component, &audioUnit) == noErr) {
        // Initialize AudioUnit instance.
    }
}
```

If the component requires asynchronous instantiation, call the [`AudioComponentInstantiate(_:_:_:)`](audiocomponentinstantiate(_:_:_:).md) function, and pass it the component you want to instantiate, the desired instantiation option (in or out of process), and a completion block that’s called when the instantiation completes. This callback block provides the audio unit instance or any errors that might have occurred while instantiating the component.

> ❗ **Important**:  Don’t block the main thread while waiting for the asynchronous instantiation to complete.

 Don’t block the main thread while waiting for the asynchronous instantiation to complete.

##### Present the Audio Units User Interface

You access an AUv2 plug-in’s user interface by retrieving its [`kAudioUnitProperty_CocoaUI`](kaudiounitproperty_cocoaui.md) property. This property isn’t used with AUv3 plug-ins; you retrieve the user interface instead using the [`kAudioUnitProperty_RequestViewController`](kaudiounitproperty_requestviewcontroller.md) property. You do so by setting a callback block that’s invoked when the framework loads the user interface. The callback provides a reference to the Audio Unit’s user interface, which you can present in your host’s interface.

```objc
AudioComponent component = ...

AudioComponentDescription componentDesc;
AudioComponentGetDescription(component, &componentDesc);

bool isAUv3 = (componentDesc.componentFlags &
               kAudioComponentFlag_IsV3AudioUnit) > 0;

if (isAUv3) {
    __block AUViewControllerBase *viewController = nil;
    
    auto callback = ^(AUViewControllerBase *vc) {
        viewController = vc;
        // Dispatch back to the main queue to embed the UI.
    };
    
    // AUv3: Retrieve the UI using the kAudioUnitProperty_RequestViewController property.
    AudioUnitSetProperty(audioUnit,
                         kAudioUnitProperty_RequestViewController,
                         kAudioUnitScope_Global,
                         0,
                         &callback,
                         sizeof(callback));
} else {
    // AUv2: Retrieve the UI using the kAudioUnitProperty_CocoaUI property.
}
```

## See Also

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)
  Update your Audio Unit (AU) host app to take advantage of the new features and capabilities of AUv3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/hosting-audio-unit-extensions-using-the-auv2-api)*