# doNotDisplay

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample should be decoded but not displayed.

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
var doNotDisplay: Bool { get set }
```

#### Discussion

Use this attachment at run time to request this behavior from a display pipeline such as the `AVSampleBufferDisplayLayer` class.

This attachment is not written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/donotdisplay)*