# UIPasteControl.DisplayMode

**Framework**: UIKit  
**Kind**: enum

Options that determine whether a paste button composes an icon, textual label, or both.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum DisplayMode
```

#### Overview

The paste button ([`UIPasteControl`](uipastecontrol.md)) property [`displayMode`](uipastecontrol/configuration-swift.class/displaymode.md) is of this type.

## Topics

### Choosing a display mode
- [UIPasteControl.DisplayMode.iconAndLabel](uipastecontrol/displaymode/iconandlabel.md)
  A display mode for a button that composes an icon and a textual label.
- [UIPasteControl.DisplayMode.iconOnly](uipastecontrol/displaymode/icononly.md)
  A display mode for an icon button.
- [UIPasteControl.DisplayMode.labelOnly](uipastecontrol/displaymode/labelonly.md)
  A display mode for a textual label.
### Enumeration Cases
- [UIPasteControl.DisplayMode.arrowAndLabel](uipastecontrol/displaymode/arrowandlabel.md)
### Initializers
- [init?(rawValue: UInt)](uipastecontrol/displaymode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIPasteControl](uipastecontrol.md)
  A button that a person taps to place pasteboard contents in your app.
- [UIPasteControl.Configuration](uipastecontrol/configuration-swift.class.md)
  An object that determines a paste button’s color, corner style, icon, and text.
- [class UIPasteboard](uipasteboard.md)
  An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [class UIPasteConfiguration](uipasteconfiguration.md)
  The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [protocol UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
  The interface that determines whether a responder object supports paste configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipastecontrol/displaymode)*