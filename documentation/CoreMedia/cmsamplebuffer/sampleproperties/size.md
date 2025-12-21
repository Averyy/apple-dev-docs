# size

**Framework**: Core Media  
**Kind**: property

Size in bytes of the sample.

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
var size: Int?
```

#### Discussion

The size of the sample is only applicable for buffers carrying data blocks. For pixel buffers and tagged buffers, the size should be set to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleproperties/size)*