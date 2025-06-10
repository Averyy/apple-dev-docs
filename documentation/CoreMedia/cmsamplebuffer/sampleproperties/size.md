# size

**Framework**: Core Media  
**Kind**: property

Size in bytes of the sample.

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
var size: Int?
```

#### Discussion

The size of the sample is only applicable for buffers carrying data blocks. For pixel buffers and tagged buffers, the size should be set to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleproperties/size)*