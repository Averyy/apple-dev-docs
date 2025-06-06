# kCGPDFContextUserPassword

**Framework**: Core Graphics  
**Kind**: var

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
let kCGPDFContextUserPassword: CFString
```

#### Discussion

The user password of the PDF document. If the document is encrypted, then the value of this key will be the user password for the document. If not specified, the user password is the empty string. The value of this key must be a CFString object that can be represented in ASCII encoding; only the first 32 bytes will be used for the password. If the value of this key cannot be represented in ASCII, the document is not created and the creation function returns `NULL`.

## See Also

- [let kCGPDFContextAuthor: CFString](kcgpdfcontextauthor.md)
  The corresponding value is a string that represents the name of the person who created the document. This key is optional.
- [let kCGPDFContextCreator: CFString](kcgpdfcontextcreator.md)
  The corresponding value is a string that represents the name of the application used to produce the document. This key is optional.
- [let kCGPDFContextTitle: CFString](kcgpdfcontexttitle.md)
  The corresponding value is a string that represents the title of the document. This key is optional.
- [let kCGPDFContextOwnerPassword: CFString](kcgpdfcontextownerpassword.md)
- [let kCGPDFContextAllowsPrinting: CFString](kcgpdfcontextallowsprinting.md)
  Whether the document allows printing when unlocked with the user password.
- [let kCGPDFContextAllowsCopying: CFString](kcgpdfcontextallowscopying.md)
  Whether the document allows copying when unlocked with the user password.
- [let kCGPDFContextOutputIntent: CFString](kcgpdfcontextoutputintent.md)
- [let kCGPDFContextOutputIntents: CFString](kcgpdfcontextoutputintents.md)
- [let kCGPDFContextSubject: CFString](kcgpdfcontextsubject.md)
- [let kCGPDFContextKeywords: CFString](kcgpdfcontextkeywords.md)
- [let kCGPDFContextEncryptionKeyLength: CFString](kcgpdfcontextencryptionkeylength.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgpdfcontextuserpassword)*