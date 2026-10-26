# INStartCallCallCapabilityUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the reason the app can’t support starting the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INStartCallCallCapabilityUnsupportedReason
```

```c
enum INStartCallCallCapabilityUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INStartCallCallCapabilityUnsupportedReason.videoCallUnsupported](./instartcallcallcapabilityunsupportedreason/videocallunsupported.md)
  The app doesn’t support video calls.
- [INStartCallCallCapabilityUnsupportedReason.microphoneNotAccessible](./instartcallcallcapabilityunsupportedreason/microphonenotaccessible.md)
  The microphone isn’t accessible.
- [INStartCallCallCapabilityUnsupportedReason.cameraNotAccessible](./instartcallcallcapabilityunsupportedreason/cameranotaccessible.md)
  The camera isn’t accessible.
### Initializers
- [init?(rawValue: Int)](./instartcallcallcapabilityunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result Object
- [init(callCapabilityResolutionResult: INCallCapabilityResolutionResult)](./instartcallcallcapabilityresolutionresult/init%28callcapabilityresolutionresult%29.md)
  Creates an object whose resolution involves the succesful start of a call with the specified capabilities.
- [class func unsupported(forReason: INStartCallCallCapabilityUnsupportedReason) -> Self](./instartcallcallcapabilityresolutionresult/unsupported%28forreason%29.md)
  Creates an object specifying that resolution of the parameter wasn’t supported, for the specified reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcallcapabilityunsupportedreason)*