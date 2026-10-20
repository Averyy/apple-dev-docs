# destination

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the destination associated with the outline.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var destination: PDFDestination? { get set }
```

```objc
@property (nonatomic, strong, nullable) PDFDestination * destination;
```

#### Discussion

The root outline serves only as a container for the outlines it owns; it does not have a destination. Note that a `PDFOutline` object can have either a destination or an action, not both.

This method may return `NULL` if the outline has an associated action instead of a destination. Note that if the associated action is a [`PDFActionGoTo`](../pdfactiongoto.md), this method returns the destination from the `PDFActionGoTo` object. However, it is better to use the [`action`](./action.md) method for this purpose.

## See Also

### Managing Actions and Destinations
- [var action: PDFAction?](./action.md)
  Returns the action performed when users click the outline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/destination)*