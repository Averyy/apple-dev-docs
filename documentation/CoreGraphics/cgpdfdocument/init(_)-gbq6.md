# init(_:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a Core Graphics PDF document using a data provider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(_ provider: CGDataProvider)
```

```c
extern CGPDFDocumentRefCGPDFDocumentCreateWithProvider(CGDataProviderRef provider);
```

## Return Value

A new Core Graphics PDF document, or `NULL` if a document can not be created. In Objective-C, you’re responsible for releasing the object using [`CGPDFDocumentRelease`](../cgpdfdocumentrelease.md).

## Discussion

Distributing individual pages of a PDF document to separate threads is not supported. If you want to use threads, consider creating a separate document for each thread and operating on a block of pages per thread.

## Parameters

- `provider`: A data provider that supplies the PDF document data.

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [CGContextDrawPDFDocument](../cgcontextdrawpdfdocument.md)
### Creating PDF Documents
- [init?(CFURL)](./init%28_%29-2gtsd.md)
  Creates a Core Graphics PDF document using data specified by a URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/init(_:)-gbq6)*