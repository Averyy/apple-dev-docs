# keywords

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

An array of keywords associated with the item, such as work, birthday, important, and so on.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var keywords: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * keywords;
```

## See Also

### Describing general attributes
- [var alternateNames: [String]?](./alternatenames.md)
  An array of localized strings that represent alternate display names for the item.
- [var contentType: String?](./contenttype.md)
  The uniform type identifier (UTI) of the item.
- [var contentTypeTree: [String]?](./contenttypetree.md)
  An attribute type that identifies a custom hierarchy of types to describe the attributes of your item.
- [var contentURL: URL?](./contenturl.md)
  The file URL of the content to index.
- [var darkThumbnailURL: URL?](./darkthumbnailurl.md)
  The local file URL of the thumbnail image for the item when Dark Mode is active.
- [var displayName: String?](./displayname.md)
  A localized string that contains the name of the item, suitable to display in the user interface.
- [var metadataModificationDate: Date?](./metadatamodificationdate.md)
  The date on which the last metadata attribute was changed.
- [var path: String?](./path.md)
  The complete path to the item.
- [var rankingHint: NSNumber?](./rankinghint.md)
  A number that indicates the relative importance of the item among other items from the app.
- [var relatedUniqueIdentifier: String?](./relateduniqueidentifier.md)
  The unique identifier for the item to which the activity is related.
- [var thumbnailData: Data?](./thumbnaildata.md)
  Image data that represents the thumbnail of the item.
- [var thumbnailURL: URL?](./thumbnailurl.md)
  The local file URL of the thumbnail image for the item.
- [var title: String?](./title.md)
  The title of the item.
- [var domainIdentifier: String?](./domainidentifier.md)
  An identifier that represents the domain or owner of the item.
- [var weakRelatedUniqueIdentifier: String?](./weakrelateduniqueidentifier.md)
  The unique identifier for the item to which the activity is related, but not linked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/keywords)*