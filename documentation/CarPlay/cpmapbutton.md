# CPMapButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that represents an action that a map template displays on the CarPlay screen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPMapButton
```

```objc
@interface CPMapButton : NSObject
```

## Topics

### Creating a Map Button
- [init(handler: ((CPMapButton) -> Void)?)](./cpmapbutton/init%28handler%29.md)
  Creates a new map button.
### Providing Button Images
- [var image: UIImage?](./cpmapbutton/image.md)
  The image to display on the button.
- [var focusedImage: UIImage?](./cpmapbutton/focusedimage.md)
  The image to display when focus is on the button.
### Controlling the Button
- [var isEnabled: Bool](./cpmapbutton/isenabled.md)
  A Boolean value that enables and disables the map button.
- [var isHidden: Bool](./cpmapbutton/ishidden.md)
  A Boolean value that hides and shows the map button.
### Initializers
- [init?(coder: NSCoder)](./cpmapbutton/init%28coder%29.md)

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
- [Sendable](../Swift/sendable.md)

## See Also

### Managing Map Buttons
- [var mapButtons: [CPMapButton]](./cpmaptemplate/mapbuttons.md)
  An array of map buttons on the trailing bottom corner of the map template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmapbutton)*