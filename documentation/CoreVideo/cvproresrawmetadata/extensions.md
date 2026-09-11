# extensions

**Framework**: Core Video  
**Kind**: property

ProRes RAW metadata extensions. This Data contains a big-endian UInt32 representing the size of the item in bytes followed by a 4-character code (‘psim’) followed by a variable-length pascal string identifying the metadata (like a key string) followed by the metadata payload.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var extensions: Data?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvproresrawmetadata/extensions)*