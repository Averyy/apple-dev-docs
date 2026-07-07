# relatedUniqueIdentifier

**Framework**: Core Spotlight  
**Kind**: property

The unique identifier for the item to which the activity is related.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var relatedUniqueIdentifier: String? { get set }
```

#### Discussion

If you’re using both [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) and Core Spotlight APIs to index the same item, set this property in the activity to specify the unique identifier of the Core Spotlight item to which the activity is related, and to avoid displaying duplicate results in Spotlight.

If the unique identifier to which the activity is related hasn’t already been indexed with Core Spotlight, the activity won’t be indexed. Note that when the item is deleted, the related activity is also deleted, unlike the behavior of [`weakRelatedUniqueIdentifier`](cssearchableitemattributeset/weakrelateduniqueidentifier.md).

## See Also

- [var alternateNames: [String]?](cssearchableitemattributeset/alternatenames.md)
  An array of localized strings that represent alternate display names for the item.
- [var contentType: String?](cssearchableitemattributeset/contenttype.md)
  The uniform type identifier (UTI) of the item.
- [var contentTypeTree: [String]?](cssearchableitemattributeset/contenttypetree.md)
  An attribute type that identifies a custom hierarchy of types to describe the attributes of your item.
- [var contentURL: URL?](cssearchableitemattributeset/contenturl.md)
  The file URL of the content to index.
- [var darkThumbnailURL: URL?](cssearchableitemattributeset/darkthumbnailurl.md)
  The local file URL of the thumbnail image for the item when Dark Mode is active.
- [var displayName: String?](cssearchableitemattributeset/displayname.md)
  A localized string that contains the name of the item, suitable to display in the user interface.
- [var keywords: [String]?](cssearchableitemattributeset/keywords.md)
  An array of keywords associated with the item, such as work, birthday, important, and so on.
- [var metadataModificationDate: Date?](cssearchableitemattributeset/metadatamodificationdate.md)
  The date on which the last metadata attribute was changed.
- [var path: String?](cssearchableitemattributeset/path.md)
  The complete path to the item.
- [var rankingHint: NSNumber?](cssearchableitemattributeset/rankinghint.md)
  A number that indicates the relative importance of the item among other items from the app.
- [var thumbnailData: Data?](cssearchableitemattributeset/thumbnaildata.md)
  Image data that represents the thumbnail of the item.
- [var thumbnailURL: URL?](cssearchableitemattributeset/thumbnailurl.md)
  The local file URL of the thumbnail image for the item.
- [var title: String?](cssearchableitemattributeset/title.md)
  The title of the item.
- [var domainIdentifier: String?](cssearchableitemattributeset/domainidentifier.md)
  An identifier that represents the domain or owner of the item.
- [var weakRelatedUniqueIdentifier: String?](cssearchableitemattributeset/weakrelateduniqueidentifier.md)
  The unique identifier for the item to which the activity is related, but not linked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/relateduniqueidentifier)*