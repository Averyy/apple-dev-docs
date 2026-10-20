# audiences

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A class of entity for which the item is intended or useful.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var audiences: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * audiences;
```

#### Discussion

A class of entity may be determined by the creator or the publisher of the item or by a third party.

## See Also

### Describing document content
- [var contentDescription: String?](./contentdescription.md)
  A description of the item’s content.
- [var creator: String?](./creator.md)
  The name of the app that created the content.
- [var encodingApplications: [String]?](./encodingapplications.md)
  The name of the apps that converted the original content into a PDF stream.
- [var fileSize: NSNumber?](./filesize.md)
  The size of the document file.
- [var fontNames: [String]?](./fontnames.md)
  An array of font names the document uses.
- [var identifier: String?](./identifier.md)
  A formal identifier that references the document the item represents.
- [var kind: String?](./kind.md)
  A description of the kind of document the item represents.
- [var pageCount: NSNumber?](./pagecount.md)
  The number of pages in the document.
- [var pageHeight: NSNumber?](./pageheight.md)
  The height of the document page, in points (72 points per inch).
- [var pageWidth: NSNumber?](./pagewidth.md)
  The width of the document page, in points (72 points per inch).
- [var securityMethod: String?](./securitymethod.md)
  The security method (a type of encryption) that protects the document file.
- [var subject: String?](./subject.md)
  The subject of the document.
- [var theme: String?](./theme.md)
  The theme of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/audiences)*