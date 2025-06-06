# init()

**Framework**: PDFKit  
**Kind**: init

Initializes a `PDFOutline` object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

#### Discussion

If you want the `PDFOutline` object returned by this method to be the outline root, you must add additional `PDFOutline` objects to create the outline hierarchy you desire. Then, you must add the root outline object to your PDF document by passing it to the `PDFDocument` `setOutlineRoot(_:)` method.

If you want the `PDFOutline` object returned by this method to be a child of an existing outline, you must use `setLabel(_:)` to give it a label and give it either a destination or action using `setDestination(_:)` or `setAction(_:)`, respectively. In addition, you must add this outline object to the existing `PDFOutline` object as a new child, using [`insertChild(_:at:)`](pdfoutline/insertchild(_:at:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/init())*