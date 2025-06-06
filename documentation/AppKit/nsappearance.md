# NSAppearance

**Framework**: AppKit  
**Kind**: class

An object that manages standard appearance attributes for UI elements in an app.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class NSAppearance
```

## Mentions

- [Choosing a Specific Appearance for Your macOS App](choosing-a-specific-appearance-for-your-macos-app.md)

#### Overview

An [`NSAppearance`](nsappearance.md) object manages how AppKit renders your app’s UI elements. Specifically, appearance objects determine which colors and images AppKit uses when drawing windows, views, and controls. Although you can use an appearance object to determine how to draw custom views and controls, a better approach is to choose colors and images that adapt automatically to the current appearance. For example, define a color asset whose actual color value changes for light and dark appearances. You can assign specific appearances to your views in Interface Builder.

The user chooses the default appearance for the system, but you can override that appearance for all or part of your app. Apps inherit the default system appearance, windows inherit their app’s appearance, and views inherit the appearance of their nearest ancestor (either a superview or window). To force a window or view to adopt an appearance, assign a specific appearance object to its [`appearance`](nsappearancecustomization/appearance.md) property.

When AppKit draws a control, it automatically sets the current appearance on the current thread to the control’s appearance. The current appearance influences the drawing path and return values you get when you access system fonts and colors. The current appearance also affects the appearance of text and images, such as the text and template images in a toolbar.

## Topics

### Creating an Appearance
- [init?(named: NSAppearance.Name)](nsappearance/init(named:).md)
  Creates an appearance object based on the name of one of the standard system appearances.
- [init?(appearanceNamed: NSAppearance.Name, bundle: Bundle?)](nsappearance/init(appearancenamed:bundle:).md)
  Creates an appearance object from the named appearance file located in the specified bundle.
- [init?(coder: NSCoder)](nsappearance/init(coder:).md)
### Getting the Appearance Name
- [var name: NSAppearance.Name](nsappearance/name-swift.property.md)
  The name of the appearance.
- [NSAppearance.Name](nsappearance/name-swift.struct.md)
### Determining the Most Appropriate Appearance
- [func bestMatch(from: [NSAppearance.Name]) -> NSAppearance.Name?](nsappearance/bestmatch(from:).md)
  Returns the appearance name that most closely matches the current appearance object.
### Getting and Setting the Current Appearance
- [class func currentDrawing() -> NSAppearance](nsappearance/currentdrawing.md)
  The appearance that the system uses for color and asset resolution, and that’s active for drawing, usually from locking focus on a view.
- [func performAsCurrentDrawingAppearance(() -> Void)](nsappearance/performascurrentdrawingappearance(_:).md)
  Sets the appearance to be the active drawing appearance and perform the specified block.
- [class var current: NSAppearance!](nsappearance/current.md)
  Returns the appearance object that’s active on the current thread.
### Managing Vibrancy
- [var allowsVibrancy: Bool](nsappearance/allowsvibrancy.md)
  Specifies whether the current appearance allows vibrancy.

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

## See Also

- [protocol NSAppearanceCustomization](nsappearancecustomization.md)
  A set of methods for getting and setting the appearance attributes of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearance)*