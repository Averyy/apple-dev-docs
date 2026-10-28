# kCGPDFContextBleedBox

**Framework**: Core Graphics  
**Kind**: var  
**Role**: Global Variable

The bleed box for the document or for a given page.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCGPDFContextBleedBox: CFString
```

```c
extern CFStringRef const kCGPDFContextBleedBox;
```

## Discussion

This key is optional. If present, the value of this key must be a [`CFData`](../CoreFoundation/cfdata.md) object that contains a [`CGRect`](../CoreFoundation/cgrect.md) (stored by value, not by reference).

## See Also

### Box Keys
- [let kCGPDFContextMediaBox: CFString](./kcgpdfcontextmediabox.md)
  The media box for the document or for a given page.
- [let kCGPDFContextCropBox: CFString](./kcgpdfcontextcropbox.md)
  The crop box for the document or for a given page.
- [let kCGPDFContextTrimBox: CFString](./kcgpdfcontexttrimbox.md)
  The trim box for the document or for a given page.
- [let kCGPDFContextArtBox: CFString](./kcgpdfcontextartbox.md)
  The art box for the document or for a given page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextbleedbox)*