# icon

**Framework**: Quick Look Thumbnailing  
**Kind**: property

A file icon representation of a file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static var icon: QLThumbnailGenerator.Request.RepresentationTypes { get }
```

#### Discussion

Files of the same type share the same file icon.

## See Also

- [init(rawValue: UInt)](qlthumbnailgenerator/request/representationtypes-swift.struct/init(rawvalue:).md)
  Creates a new thumbnail type object for a given value.
- [static var all: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct/all.md)
  The thumbnail type to generate all possible thumbnail representations.
- [static var lowQualityThumbnail: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct/lowqualitythumbnail.md)
  A faster to generate version of the thumbnail that may sacrifice quality for speed.
- [static var thumbnail: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct/thumbnail.md)
  A thumbnail representation of a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/representationtypes-swift.struct/icon)*