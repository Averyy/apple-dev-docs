# RPBroadcastActivityController

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

A controller object that presents the macOS broadcast picker.

**Availability**:
- macOS 11.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
class RPBroadcastActivityController
```

```objc
@interface RPBroadcastActivityController : NSObject
```

## Topics

### Showing a Broadcast Picker
- [class func showBroadcastPicker(at: CGPoint, from: NSWindow?, preferredExtensionIdentifier: String?, completionHandler: (RPBroadcastActivityController?, (any Error)?) -> Void)](./rpbroadcastactivitycontroller/showbroadcastpicker%28at,from,preferredextensionidentifier,completionhandler%29.md)
  Presents a list of available broadcast services for the user to select.
### Accessing the Delegate Object
- [var delegate: (any RPBroadcastActivityControllerDelegate)?](./rpbroadcastactivitycontroller/delegate.md)
  The broadcast activity controller’s delegate object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Live Broadcast Implementation
- [class RPBroadcastActivityViewController](./rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPSystemBroadcastPickerView](./rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](./rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- [class RPBroadcastConfiguration](./rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontroller)*