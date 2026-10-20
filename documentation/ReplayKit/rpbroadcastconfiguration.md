# RPBroadcastConfiguration

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

An object used to configure the movie clips produced during a live broadcast.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
class RPBroadcastConfiguration
```

```objc
@interface RPBroadcastConfiguration : NSObject
```

## Topics

### Configuring Movie Clips
- [var clipDuration: TimeInterval](./rpbroadcastconfiguration/clipduration.md)
  The duration of movie clips sent the to the movie clip handler extension.
- [var videoCompressionProperties: [String : any NSSecureCoding & NSObjectProtocol]?](./rpbroadcastconfiguration/videocompressionproperties.md)
  The compression properties for encoding movie clips that are to be overwritten.
### Initializers
- [init?(coder: NSCoder)](./rpbroadcastconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Live Broadcast Implementation
- [class RPBroadcastActivityViewController](./rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPSystemBroadcastPickerView](./rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [class RPBroadcastActivityController](./rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](./rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration)*