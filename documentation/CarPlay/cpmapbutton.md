# CPMapButton

**Framework**: CarPlay  
**Kind**: class

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

## Topics

### Creating a Map Button
- [init(handler: ((CPMapButton) -> Void)?)](cpmapbutton/init(handler:).md)
  Creates a new map button.
### Providing Button Images
- [var image: UIImage?](cpmapbutton/image.md)
  The image to display on the button.
- [var focusedImage: UIImage?](cpmapbutton/focusedimage.md)
  The image to display when focus is on the button.
### Controlling the Button
- [var isEnabled: Bool](cpmapbutton/isenabled.md)
  A Boolean value that enables and disables the map button.
- [var isHidden: Bool](cpmapbutton/ishidden.md)
  A Boolean value that hides and shows the map button.

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

- [var mapButtons: [CPMapButton]](cpmaptemplate/mapbuttons.md)
  An array of map buttons on the trailing bottom corner of the map template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmapbutton)*