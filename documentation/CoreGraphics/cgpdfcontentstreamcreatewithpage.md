# CGPDFContentStreamCreateWithPage(_:)

**Framework**: Core Graphics  
**Kind**: func

Creates a content stream object from a PDF page object.

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
func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage) -> CGPDFContentStreamRef
```

#### Return Value

A new [`CGPDFContentStreamRef`](cgpdfcontentstreamref.md) object. In Objective-C, you’re responsible for releasing this object by calling the [`CGPDFContentStreamRelease(_:)`](cgpdfcontentstreamrelease(_:).md) function.

#### Discussion

A [`CGPDFContentStreamRef`](cgpdfcontentstreamref.md) object can contain more than one PDF content stream. To retrieve an array of the PDF content streams in the object, call the function [`CGPDFContentStreamGetStreams(_:)`](cgpdfcontentstreamgetstreams(_:).md). To obtain the resources associated with a [`CGPDFContentStreamRef`](cgpdfcontentstreamref.md) object, call the function [`CGPDFContentStreamGetResource(_:_:_:)`](cgpdfcontentstreamgetresource(_:_:_:).md).

## Parameters

- `page`: A PDF page object.

## See Also

- [func CGPDFContentStreamCreateWithStream(CGPDFStreamRef, CGPDFDictionaryRef, CGPDFContentStreamRef) -> CGPDFContentStreamRef](cgpdfcontentstreamcreatewithstream(_:_:_:).md)
  Creates a PDF content stream object from an existing PDF content stream object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamcreatewithpage(_:))*