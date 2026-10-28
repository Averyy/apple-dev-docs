# ceilMode

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

Affects how MPSGraph computes the output size: if set to `YES` then output size is computed by rounding up instead of down when dividing input size by stride.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var ceilMode: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL ceilMode;
```

## Discussion

Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/ceilmode)*