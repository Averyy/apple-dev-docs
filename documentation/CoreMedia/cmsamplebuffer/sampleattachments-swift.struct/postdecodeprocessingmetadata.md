# postDecodeProcessingMetadata

**Framework**: Core Media  
**Kind**: property

Represents the sequence and frame level metadata for post decode processing. This attachment is used to pass sequence and frame level metadata from a format reader to a decoder or RAW processor. The value should only contain plist types.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var postDecodeProcessingMetadata: [String : any Sendable]? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/postdecodeprocessingmetadata)*