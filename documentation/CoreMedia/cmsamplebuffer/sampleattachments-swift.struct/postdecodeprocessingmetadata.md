# postDecodeProcessingMetadata

**Framework**: Core Media  
**Kind**: property

Represents the sequence and frame level metadata for post decode processing. This attachment is used to pass sequence and frame level metadata from a format reader to a decoder or RAW processor. The value should only contain plist types.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var postDecodeProcessingMetadata: [String : any Sendable]? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/postdecodeprocessingmetadata)*