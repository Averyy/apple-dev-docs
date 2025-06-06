# kCGPDFContextOutputIntents

**Framework**: Core Graphics  
**Kind**: var

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.4+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let kCGPDFContextOutputIntents: CFString
```

#### Discussion

Output intent dictionaries. This key is optional. If present, the value must be an array of one or more [`kCGPDFContextOutputIntent`](kcgpdfcontextoutputintent.md) dictionaries. The array is added to the PDF document in the `/OutputIntents` entry in the PDF file’s document catalog. Each dictionary in the array must be of form specified for the [`kCGPDFContextOutputIntent`](kcgpdfcontextoutputintent.md) key, except that only the first dictionary in the array is required to contain the “S” key with a value of `GTS_PDFX`. If both the [`kCGPDFContextOutputIntent`](kcgpdfcontextoutputintent.md) and [`kCGPDFContextOutputIntents`](kcgpdfcontextoutputintents.md) keys are specified, the former is ignored.

## See Also

- [let kCGPDFContextAuthor: CFString](kcgpdfcontextauthor.md)
  The corresponding value is a string that represents the name of the person who created the document. This key is optional.
- [let kCGPDFContextCreator: CFString](kcgpdfcontextcreator.md)
  The corresponding value is a string that represents the name of the application used to produce the document. This key is optional.
- [let kCGPDFContextTitle: CFString](kcgpdfcontexttitle.md)
  The corresponding value is a string that represents the title of the document. This key is optional.
- [let kCGPDFContextOwnerPassword: CFString](kcgpdfcontextownerpassword.md)
- [let kCGPDFContextUserPassword: CFString](kcgpdfcontextuserpassword.md)
- [let kCGPDFContextAllowsPrinting: CFString](kcgpdfcontextallowsprinting.md)
  Whether the document allows printing when unlocked with the user password.
- [let kCGPDFContextAllowsCopying: CFString](kcgpdfcontextallowscopying.md)
  Whether the document allows copying when unlocked with the user password.
- [let kCGPDFContextOutputIntent: CFString](kcgpdfcontextoutputintent.md)
- [let kCGPDFContextSubject: CFString](kcgpdfcontextsubject.md)
- [let kCGPDFContextKeywords: CFString](kcgpdfcontextkeywords.md)
- [let kCGPDFContextEncryptionKeyLength: CFString](kcgpdfcontextencryptionkeylength.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextoutputintents)*