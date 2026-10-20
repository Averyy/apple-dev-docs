# nearest

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

Nearest neighbor interpolation filter.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let nearest: CALayerContentsFilter
```

```c
extern CALayerContentsFilter const kCAFilterNearest;
```

## See Also

### Constants
- [static let linear: CALayerContentsFilter](./linear.md)
  Linear interpolation filter.
- [static let trilinear: CALayerContentsFilter](./trilinear.md)
  Trilinear minification filter. Enables mipmap generation. Some renderers may ignore this, or impose additional restrictions, such as source images requiring power-of-two dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayercontentsfilter/nearest)*