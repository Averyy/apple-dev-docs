# Auxiliary Dictionary Keys

**Framework**: Core Graphics

Keys for the auxiliary info dictionary you specify when creating a PDF context.

#### Overview

For more information about using these keys in a PDF context, see [`init(consumer:mediaBox:_:)`](cgcontext/init(consumer:mediabox:_:).md) and [`init(_:mediaBox:_:)`](cgcontext/init(_:mediabox:_:).md).

## Topics

### Metadata Keys
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
- [let kCGPDFContextOutputIntents: CFString](kcgpdfcontextoutputintents.md)
- [let kCGPDFContextSubject: CFString](kcgpdfcontextsubject.md)
- [let kCGPDFContextKeywords: CFString](kcgpdfcontextkeywords.md)
- [let kCGPDFContextEncryptionKeyLength: CFString](kcgpdfcontextencryptionkeylength.md)
### Box Keys
- [let kCGPDFContextMediaBox: CFString](kcgpdfcontextmediabox.md)
  The media box for the document or for a given page.
- [let kCGPDFContextCropBox: CFString](kcgpdfcontextcropbox.md)
  The crop box for the document or for a given page.
- [let kCGPDFContextBleedBox: CFString](kcgpdfcontextbleedbox.md)
  The bleed box for the document or for a given page.
- [let kCGPDFContextTrimBox: CFString](kcgpdfcontexttrimbox.md)
  The trim box for the document or for a given page.
- [let kCGPDFContextArtBox: CFString](kcgpdfcontextartbox.md)
  The art box for the document or for a given page.
### Output Intent Keys
- [let kCGPDFXOutputIntentSubtype: CFString](kcgpdfxoutputintentsubtype.md)
  The output intent subtype. This key is required.
- [let kCGPDFXOutputConditionIdentifier: CFString](kcgpdfxoutputconditionidentifier.md)
- [let kCGPDFXOutputCondition: CFString](kcgpdfxoutputcondition.md)
  A text string identifying the intended output device or production condition in a human-readable form.
- [let kCGPDFXRegistryName: CFString](kcgpdfxregistryname.md)
- [let kCGPDFXInfo: CFString](kcgpdfxinfo.md)
- [let kCGPDFXDestinationOutputProfile: CFString](kcgpdfxdestinationoutputprofile.md)

## See Also

- [init?(CFURL, mediaBox: UnsafePointer<CGRect>?, CFDictionary?)](cgcontext/init(_:mediabox:_:).md)
  Creates a URL-based PDF graphics context.
- [init?(consumer: CGDataConsumer, mediaBox: UnsafePointer<CGRect>?, CFDictionary?)](cgcontext/init(consumer:mediabox:_:).md)
  Creates a PDF graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/auxiliary-dictionary-keys)*