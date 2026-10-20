# NSScrubberSelectionStyle

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An abstract class that provides decorative accessory views for selected and highlighted items within a scrubber control.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSScrubberSelectionStyle
```

```objc
@interface NSScrubberSelectionStyle : NSObject
```

#### Overview

Choose a selection style ([`outlineOverlay`](./nsscrubberselectionstyle/outlineoverlay.md) or [`roundedBackground`](./nsscrubberselectionstyle/roundedbackground.md)), or create a custom selection style by subclassing [`NSScrubberSelectionStyle`](./nsscrubberselectionstyle.md) and overriding [`makeSelectionView()`](./nsscrubberselectionstyle/makeselectionview%28%29.md).

## Topics

### Using built-in styles
- [class var outlineOverlay: NSScrubberSelectionStyle](./nsscrubberselectionstyle/outlineoverlay.md)
  A built-in selection style that draws the outline of the scrubber item.
- [class var roundedBackground: NSScrubberSelectionStyle](./nsscrubberselectionstyle/roundedbackground.md)
  A built-in selection style that draws a rounded rectangle as the background of the scrubber item.
### Creating a selection style
- [init()](./nsscrubberselectionstyle/init%28%29.md)
  Initializes a new scrubber selection style.
- [init(coder: NSCoder)](./nsscrubberselectionstyle/init%28coder%29.md)
  Initializes a scrubber selection style when included from a nib or Storyboard.
- [func makeSelectionView() -> NSScrubberSelectionView?](./nsscrubberselectionstyle/makeselectionview%28%29.md)
  Provides an opportunity to create a customized scrubber selection style.

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
- [Sendable](../Swift/sendable.md)

## See Also

### Scrubber items
- [class NSScrubberItemView](./nsscrubberitemview.md)
  An item at a specific index position in the scrubber.
- [class NSScrubberArrangedView](./nsscrubberarrangedview.md)
  An abstract base class for the views whose layout is managed by a scrubber.
- [class NSScrubberImageItemView](./nsscrubberimageitemview.md)
  A concrete view subclass for displaying images in a scrubber items.
- [class NSScrubberSelectionView](./nsscrubberselectionview.md)
  An abstract base class for specifying the appearance of a highlighted or selected item in a scrubber.
- [class NSScrubberTextItemView](./nsscrubbertextitemview.md)
  A concrete view subclass for displaying text for an item in a scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberselectionstyle)*