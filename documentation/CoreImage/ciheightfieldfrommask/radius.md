# radius

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The length of the height-field transition.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var radius: Float { get set }
```

```objc
@property (nonatomic) float radius;
```

## Discussion

Larger values make the transition smoother and more pronounced. Smaller values make the transition approximate a fillet radius.

## See Also

### Instance Properties
- [var inputImage: CIImage?](./inputimage.md)
  The image to use as an input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciheightfieldfrommask/radius)*