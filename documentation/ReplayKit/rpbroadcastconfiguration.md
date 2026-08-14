# RPBroadcastConfiguration

**Framework**: ReplayKit  
**Kind**: class

An object used to configure the movie clips produced during a live broadcast.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class RPBroadcastConfiguration
```

## Topics

### Configuring Movie Clips
- [var clipDuration: TimeInterval](rpbroadcastconfiguration/clipduration.md)
  The duration of movie clips sent the to the movie clip handler extension.
- [var videoCompressionProperties: [String : any NSSecureCoding & NSObjectProtocol]?](rpbroadcastconfiguration/videocompressionproperties.md)
  The compression properties for encoding movie clips that are to be overwritten.
### Initializers
- [init?(coder: NSCoder)](rpbroadcastconfiguration/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class RPBroadcastActivityViewController](rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPSystemBroadcastPickerView](rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [class RPBroadcastActivityController](rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration)*