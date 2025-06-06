# levelsOfDetail

**Framework**: Core Animation  
**Kind**: property

The number of levels of detail maintained by this layer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var levelsOfDetail: Int { get set }
```

#### Discussion

Defaults to 1. Each level of detail is half the resolution of the previous level. If too many levels are specified for the current size of the layer, then the number of levels is clamped to the maximum value (the bottom most level of detail must contain at least a single pixel in each dimension.)

## See Also

- [var levelsOfDetailBias: Int](catiledlayer/levelsofdetailbias.md)
  The number of magnified levels of detail for this layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catiledlayer/levelsofdetail)*