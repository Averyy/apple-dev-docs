# displayImmediately

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample should be displayed immediately.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var displayImmediately: Bool { get set }
```

#### Discussion

If this key is present, the sample should be displayed as soon as possible rather than according to its presentation timestamp. Use this attachment at run time to request this behavior from a display pipeline such as the `AVSampleBufferDisplayLayer` class.

This attachment is not written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/displayimmediately)*