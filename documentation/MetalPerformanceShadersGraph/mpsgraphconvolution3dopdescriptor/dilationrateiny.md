# dilationRateInY

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The amount by which weights tensor expands in the `y`-direction.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
var dilationRateInY: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger dilationRateInY;
```

#### Discussion

The weights tensor is dilated by inserting `dilationRateInY-1` zeros between consecutive values in `y`-dimension. Dilated weights tensor width is `(dilationRateInY-1)*kernelHeight+1`. Default value is 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/dilationrateiny)*