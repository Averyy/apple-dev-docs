# deliveryType

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The delivery type of the file.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var deliveryType: NSNumber? { get set }
```

```objc
@property (strong, nullable) NSNumber * deliveryType;
```

#### Discussion

The value of this property is 0 for fast start and 1 for RTSP.

## See Also

### Describing media
- [var comment: String?](./comment.md)
  A comment related to the media file.
- [var contentCreationDate: Date?](./contentcreationdate.md)
  The creation date of an edited or optimized version of the song or composition.
- [var contentModificationDate: Date?](./contentmodificationdate.md)
  The date on which the contents of the file was last modified.
- [var contentSources: [String]?](./contentsources.md)
  An array of sources from which the media was obtained.
- [var copyright: String?](./copyright.md)
  The copyright date of the content.
- [var downloadedDate: Date?](./downloadeddate.md)
  The most recent date on which the file was downloaded or received.
- [var editors: [String]?](./editors.md)
  A list of editors who have worked on the file.
- [var lastUsedDate: Date?](./lastuseddate.md)
  The date on which the file was last used.
- [var participants: [String]?](./participants.md)
  A list of people who are visible in an image or movie or written about in a document.
- [var projects: [String]?](./projects.md)
  A list of projects of which this file is a part.
- [var addedDate: Date?](./addeddate.md)
  The date on which the item was moved into its current location.
- [var codecs: [String]?](./codecs.md)
  The codecs used to encode/decode the media.
- [var contactKeywords: [String]?](./contactkeywords.md)
  A list of contacts who are associated with the content in some way, not including the author.
- [var duration: NSNumber?](./duration.md)
  The duration (if appropriate) of the content of the file, in seconds.
- [var mediaTypes: [String]?](./mediatypes.md)
  The media types present in the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/deliverytype)*