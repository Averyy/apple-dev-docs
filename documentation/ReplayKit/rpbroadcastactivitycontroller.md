# RPBroadcastActivityController

**Framework**: ReplayKit  
**Kind**: class

A controller object that presents the macOS broadcast picker.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class RPBroadcastActivityController
```

## Topics

### Showing a Broadcast Picker
- [class func showBroadcastPicker(at: CGPoint, from: NSWindow?, preferredExtensionIdentifier: String?, completionHandler: (RPBroadcastActivityController?, (any Error)?) -> Void)](rpbroadcastactivitycontroller/showbroadcastpicker(at:from:preferredextensionidentifier:completionhandler:).md)
  Presents a list of available broadcast services for the user to select.
### Accessing the Delegate Object
- [var delegate: (any RPBroadcastActivityControllerDelegate)?](rpbroadcastactivitycontroller/delegate.md)
  The broadcast activity controller’s delegate object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class RPBroadcastActivityViewController](rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPSystemBroadcastPickerView](rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- [class RPBroadcastConfiguration](rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontroller)*