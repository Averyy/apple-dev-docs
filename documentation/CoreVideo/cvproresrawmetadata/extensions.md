# extensions

**Framework**: Core Video  
**Kind**: property

ProRes RAW metadata extensions. This Data contains a big-endian UInt32 representing the size of the item in bytes followed by a 4-character code (‘psim’) followed by a variable-length pascal string identifying the metadata (like a key string) followed by the metadata payload.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var extensions: Data?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvproresrawmetadata/extensions)*