# instantiate(with:options:completionHandler:)

**Framework**: Audiotoolbox  
**Kind**: method

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
class func instantiate(with componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions = []) async throws -> AUAudioUnit
```

#### Discussion

Certain types of audio units must be instantiated asynchronously, such as version 3 units with a view.

> **Note**:  Do not block the main thread while waiting for the completion handler to be called; this can deadlock.

## Parameters

- `componentDescription`: The component to instantiate.
- `options`: Options for loading the unit in-process or out-of-process.
- `completionHandler`: The block called when instantiation has completed. The block parameters are defined as follows:

## See Also

- [convenience init(componentDescription: AudioComponentDescription) throws](auaudiounit/init(componentdescription:).md)
  Synchronously initializes a new audio unit object.
- [init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions) throws](auaudiounit/init(componentdescription:options:).md)
  Synchronously initializes a new audio unit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/instantiate(with:options:completionhandler:))*