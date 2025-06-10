# maximumInputImageDimension

**Framework**: RealityKit  
**Kind**: property

The maximum allowed dimension (either height or width) of input images that can be ingested by the reconstruction session. If images larger than this are provided, they will be ignored and an `.invalidSample` message will be output.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var maximumInputImageDimension: Int { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/limits-swift.struct/maximuminputimagedimension)*