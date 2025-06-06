# action

**Framework**: PDFKit  
**Kind**: property

Returns the action performed when users click the outline.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var action: PDFAction? { get set }
```

#### Discussion

The root outline serves only as a container for the outlines it owns; it does not have an action. Note that a `PDFOutline` object can have either an action or a destination, not both.

If the `PDFOutline` object has a destination, instead of an action,  `action` returns a [`PDFActionGoTo`](pdfactiongoto.md) object (this is equivalent to calling [`destination`](pdfoutline/destination.md) on the `PDFOutline` object). For other action types, `action` returns the appropriate PDF Kit action type object, such as [`PDFActionURL`](pdfactionurl.md).

## See Also

- [var destination: PDFDestination?](pdfoutline/destination.md)
  Returns the destination associated with the outline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/action)*