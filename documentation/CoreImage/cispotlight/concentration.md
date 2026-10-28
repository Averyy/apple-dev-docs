# concentration

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The size of the spotlight.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var concentration: Float { get set }
```

```objc
@property (nonatomic) float concentration;
```

## Discussion

The smaller the value, the more tightly focused the light beam.

## See Also

### Instance Properties
- [var brightness: Float](./brightness.md)
  The brightness of the spotlight.
- [var color: CIColor](./color.md)
  The color of the spotlight.
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.
- [var lightPointsAt: CIVector](./lightpointsat.md)
  The x and y position that the spotlight points at.
- [var lightPosition: CIVector](./lightposition.md)
  The x and y position of the spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cispotlight/concentration)*