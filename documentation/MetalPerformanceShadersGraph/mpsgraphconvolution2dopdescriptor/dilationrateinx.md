# dilationRateInX

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The amount by which the weights tensor expands in the `x`-direction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dilationRateInX: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger dilationRateInX;
```

## Discussion

The weights tensor is dilated by inserting `dilationRateInX-1` zeros between consecutive values in `x`-dimension. Dilated weights tensor width is `(dilationRateInX-1)*kernelWidth+1`. Default value is 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/dilationrateinx)*