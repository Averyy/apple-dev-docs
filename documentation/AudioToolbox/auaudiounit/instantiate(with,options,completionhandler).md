# instantiate(with:options:completionHandler:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Type Method

Asynchronously creates an audio unit instance.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func instantiate(with componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions = [], completionHandler: @escaping @Sendable (AUAudioUnit?, (any Error)?) -> Void)
```

```swift
class func instantiate(with componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions = []) async throws -> AUAudioUnit
```

```objc
+ (void) instantiateWithComponentDescription:(AudioComponentDescription) componentDescription options:(AudioComponentInstantiationOptions) options completionHandler:(void (^)(AUAudioUnit *audioUnit, NSError *error)) completionHandler;
```

## Discussion

Certain types of audio units must be instantiated asynchronously, such as version 3 units with a view.

> **Note**:  Do not block the main thread while waiting for the completion handler to be called; this can deadlock.

## Parameters

- `componentDescription`: The component to instantiate.
- `options`: Options for loading the unit in-process or out-of-process.
- `completionHandler`: The block called when instantiation has completed. The block parameters are defined as follows:

  - **audioUnit**: An initialized audio unit if the operation succeeded, or `nil` if it failed.
  - **error**: An error if the operation failed, or `nil` if it succeeded.

## See Also

### Creating an Audio Unit
- [convenience init(componentDescription: AudioComponentDescription) throws](./init%28componentdescription%29.md)
  Synchronously initializes a new audio unit object.
- [init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions) throws](./init%28componentdescription,options%29.md)
  Synchronously initializes a new audio unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/instantiate(with:options:completionhandler:))*