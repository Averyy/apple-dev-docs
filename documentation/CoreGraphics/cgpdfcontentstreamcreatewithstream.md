# CGPDFContentStreamCreateWithStream(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Creates a PDF content stream object from an existing PDF content stream object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStreamRef, _ streamResources: CGPDFDictionaryRef, _ parent: CGPDFContentStreamRef) -> CGPDFContentStreamRef
```

#### Return Value

A PDF content stream object created from the `stream` parameter. In Objective-C, you’re responsible for releasing this object by calling the [`CGPDFContentStreamRelease(_:)`](cgpdfcontentstreamrelease(_:).md) function.

#### Discussion

You can use this function to get access to the contents of a form, pattern, Type3 font, or any PDF stream.

## Parameters

- `stream`: The PDF stream you want to create a content stream from.
- `streamResources`: A PDF dictionary that contains the resources associated with the stream you want to retrieve.
- `parent`: The content stream of the page on which   appears. Supply the   parameter when you create a content stream that’s used within a page.

## See Also

- [func CGPDFContentStreamCreateWithPage(CGPDFPage) -> CGPDFContentStreamRef](cgpdfcontentstreamcreatewithpage(_:).md)
  Creates a content stream object from a PDF page object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamcreatewithstream(_:_:_:))*