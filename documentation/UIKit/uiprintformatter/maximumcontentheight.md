# maximumContentHeight

**Framework**: UIKit  
**Kind**: property

The maximum height of the content area.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var maximumContentHeight: CGFloat { get set }
```

#### Discussion

`UIPrintFormatter` uses this value to determine where the content rectangle begins on the first page. It compares the value of this property with the printing rectangle’s height minus the header and footer heights and the top inset value (of [`contentInsets`](uiprintformatter/contentinsets.md)); it uses the lower of the two values. The default value of this property is the maximum float value.

## See Also

- [var perPageContentInsets: UIEdgeInsets](uiprintformatter/perpagecontentinsets.md)
  The margins for each printed page.
- [var maximumContentWidth: CGFloat](uiprintformatter/maximumcontentwidth.md)
  The maximum width of the content area.
- [var contentInsets: UIEdgeInsets](uiprintformatter/contentinsets.md)
  The distances the edges of content are inset from the printing rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/maximumcontentheight)*