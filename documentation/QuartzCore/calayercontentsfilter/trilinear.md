# trilinear

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

Trilinear minification filter. Enables mipmap generation. Some renderers may ignore this, or impose additional restrictions, such as source images requiring power-of-two dimensions.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let trilinear: CALayerContentsFilter
```

```c
extern CALayerContentsFilter const kCAFilterTrilinear;
```

## See Also

### Constants
- [static let linear: CALayerContentsFilter](./linear.md)
  Linear interpolation filter.
- [static let nearest: CALayerContentsFilter](./nearest.md)
  Nearest neighbor interpolation filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayercontentsfilter/trilinear)*