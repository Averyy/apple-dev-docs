# UIMarkupTextPrintFormatter

**Framework**: UIKit  
**Kind**: class

An object that lays out HTML text for a multipage print job.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMarkupTextPrintFormatter
```

#### Overview

To use this print formatter for a print job, create an instance of [`UIMarkupTextPrintFormatter`](uimarkuptextprintformatter.md) initialized with the HTML, set the inherited layout properties, and add the object to the print job in one of two ways:

- If a single print formatter is being used for the print job (with no additional drawing), assign it to the [`printFormatter`](uiprintinteractioncontroller/printformatter.md) property of the [`UIPrintInteractionController`](uiprintinteractioncontroller.md) shared instance.  The inherited [`startPage`](uiprintformatter/startpage.md) property identifies the beginning page of content with which the formatter is associated.
- If you are using multiple formatters along with a page renderer, associate each print formatter with a starting page of the printed content. You often take this approach when you want to add content such as headers and footers to what the formatters provide. You have two ways of associating a print formatter with a  [`UIPrintPageRenderer`](uiprintpagerenderer.md) object:
- You can add print formatters to the [`printFormatters`](uiprintpagerenderer/printformatters.md) property of the [`UIPrintPageRenderer`](uiprintpagerenderer.md) object; the [`startPage`](uiprintformatter/startpage.md) property of the print formatter specifies the starting page.
- You can add print formatters by calling [`addPrintFormatter(_:startingAtPageAt:)`](uiprintpagerenderer/addprintformatter(_:startingatpageat:).md) for each print formatter; the second parameter of this method specifies the starting page (and overrides any [`startPage`](uiprintformatter/startpage.md) value).

You can change the markup text at any time before the drawing of the printable content begins.

## Topics

### Creating a markup-text print formatter
- [init(markupText: String)](uimarkuptextprintformatter/init(markuptext:).md)
  Returns a markup-text print formatter initialized with an HTML string.
### Getting and setting the markup text
- [var markupText: String?](uimarkuptextprintformatter/markuptext.md)
  The HTML markup text for the print formatter.

## Relationships

### Inherits From
- [UIPrintFormatter](uiprintformatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIPrintFormatter](uiprintformatter.md)
  An abstract base class for print formatters, which are objects that lay out custom printable content that can cross page boundaries.
- [class UIViewPrintFormatter](uiviewprintformatter.md)
  An object that lays out the drawn content of a view for printing.
- [class UISimpleTextPrintFormatter](uisimpletextprintformatter.md)
  An object that lays out plain text for printing, possibly over multiple pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimarkuptextprintformatter)*