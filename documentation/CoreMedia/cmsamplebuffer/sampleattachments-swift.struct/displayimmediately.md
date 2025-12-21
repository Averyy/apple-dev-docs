# displayImmediately

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample should be displayed immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var displayImmediately: Bool { get set }
```

#### Discussion

If this key is present, the sample should be displayed as soon as possible rather than according to its presentation timestamp. Use this attachment at run time to request this behavior from a display pipeline such as the `AVSampleBufferDisplayLayer` class.

This attachment is not written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/displayimmediately)*