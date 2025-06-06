# UIPasteControl.Configuration

**Framework**: UIKit  
**Kind**: class

An object that determines a paste button’s color, corner style, icon, and text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class Configuration
```

#### Overview

The paste button ([`UIPasteControl`](uipastecontrol.md)) property [`configuration`](uipastecontrol/configuration-swift.property.md) is of this type.

## Topics

### Coloring the button
- [var baseBackgroundColor: UIColor?](uipastecontrol/configuration-swift.class/basebackgroundcolor.md)
  A color for the paste button’s background.
- [var baseForegroundColor: UIColor?](uipastecontrol/configuration-swift.class/baseforegroundcolor.md)
  A color for the paste button’s icon and text.
### Shaping button corners
- [var cornerRadius: CGFloat](uipastecontrol/configuration-swift.class/cornerradius.md)
  A value that rounds the edges of a paste button.
- [var cornerStyle: UIButton.Configuration.CornerStyle](uipastecontrol/configuration-swift.class/cornerstyle.md)
  A shape for the button among a predetermined set of templates.
### Choosing control icon and text
- [var displayMode: UIPasteControl.DisplayMode](uipastecontrol/configuration-swift.class/displaymode.md)
  An option that determines whether the paste button composes an icon, textual label, or both.
- [UIPasteControl.DisplayMode](uipastecontrol/displaymode.md)
  Options that determine whether a paste button composes an icon, textual label, or both.
### Instance Properties
- [var imagePlacement: NSDirectionalRectEdge](uipastecontrol/configuration-swift.class/imageplacement.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPasteControl](uipastecontrol.md)
  A button that a person taps to place pasteboard contents in your app.
- [UIPasteControl.DisplayMode](uipastecontrol/displaymode.md)
  Options that determine whether a paste button composes an icon, textual label, or both.
- [class UIPasteboard](uipasteboard.md)
  An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [class UIPasteConfiguration](uipasteconfiguration.md)
  The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [protocol UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
  The interface that determines whether a responder object supports paste configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipastecontrol/configuration-swift.class)*