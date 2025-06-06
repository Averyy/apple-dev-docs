# compare(_:)

**Framework**: PDFKit  
**Kind**: method

Returns a comparison result that indicates the location of the destination in the document, relative to the current position.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func compare(_ destination: PDFDestination) -> ComparisonResult
```

#### Return Value

A comparison result, indicating the position of the passed-in destination relative to the current position.

#### Discussion

If `destination` is between the receiver’s position and the end of the document, `compare` returns `NSOrderedAscending`; if it is between the receiver’s position and the beginning of the document, `compare` returns `NSOrderedDescending`. Otherwise, if `destination` matches the receiver’s position, `compare` returns `NSOrderedSame`.

This method ignores the horizontal component of the destination point (the x value). If the destination’s vertical component (or y value) is [`PDFDestination`](pdfdestination.md), `compare` treats the destination as if its y value is the top point on the destination page.

An exception is raised if `destination` does not have a page associated with it or if its page is associated with a document other than the receiver’s document.

## Parameters

- `destination`: The destination in the document to be located.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdestination/compare(_:))*