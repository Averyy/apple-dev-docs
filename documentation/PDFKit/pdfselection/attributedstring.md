# attributedString

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns an `NSAttributedString` object representing the text contained in the selection (may contain linefeed characters).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var attributedString: NSAttributedString? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSAttributedString * attributedString;
```

## See Also

### Getting Information About a Selection
- [var pages: [PDFPage]](./pages.md)
  Returns the array of pages contained in the selection.
- [var string: String?](./string.md)
  Returns an `NSString` object representing the text contained in the selection (may contain linefeed characters).
- [func bounds(for: PDFPage) -> CGRect](./bounds%28for%29.md)
  Returns the bounds of the selection on the specified page.
- [func selectionsByLine() -> [PDFSelection]](./selectionsbyline%28%29.md)
  Returns an array of selections, one for each line of text covered by the receiver.
- [var color: UIColor?](./color.md)
  Sets the color used for the drawing of a selection in both active and inactive states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfselection/attributedstring)*