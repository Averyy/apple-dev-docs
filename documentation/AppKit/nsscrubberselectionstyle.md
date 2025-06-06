# NSScrubberSelectionStyle

**Framework**: AppKit  
**Kind**: class

An abstract class that provides decorative accessory views for selected and highlighted items within a scrubber control.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSScrubberSelectionStyle
```

#### Overview

Choose a selection style ([`outlineOverlay`](nsscrubberselectionstyle/outlineoverlay.md) or [`roundedBackground`](nsscrubberselectionstyle/roundedbackground.md)), or create a custom selection style by subclassing [`NSScrubberSelectionStyle`](nsscrubberselectionstyle.md) and overriding [`makeSelectionView()`](nsscrubberselectionstyle/makeselectionview().md).

## Topics

### Using built-in styles
- [class var outlineOverlay: NSScrubberSelectionStyle](nsscrubberselectionstyle/outlineoverlay.md)
  A built-in selection style that draws the outline of the scrubber item.
- [class var roundedBackground: NSScrubberSelectionStyle](nsscrubberselectionstyle/roundedbackground.md)
  A built-in selection style that draws a rounded rectangle as the background of the scrubber item.
### Creating a selection style
- [init()](nsscrubberselectionstyle/init.md)
  Initializes a new scrubber selection style.
- [init(coder: NSCoder)](nsscrubberselectionstyle/init(coder:).md)
  Initializes a scrubber selection style when included from a nib or Storyboard.
- [func makeSelectionView() -> NSScrubberSelectionView?](nsscrubberselectionstyle/makeselectionview.md)
  Provides an opportunity to create a customized scrubber selection style.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSScrubberItemView](nsscrubberitemview.md)
  An item at a specific index position in the scrubber.
- [class NSScrubberArrangedView](nsscrubberarrangedview.md)
  An abstract base class for the views whose layout is managed by a scrubber.
- [class NSScrubberImageItemView](nsscrubberimageitemview.md)
  A concrete view subclass for displaying images in a scrubber items.
- [class NSScrubberSelectionView](nsscrubberselectionview.md)
  An abstract base class for specifying the appearance of a highlighted or selected item in a scrubber.
- [class NSScrubberTextItemView](nsscrubbertextitemview.md)
  A concrete view subclass for displaying text for an item in a scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberselectionstyle)*