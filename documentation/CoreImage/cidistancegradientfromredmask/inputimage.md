# inputImage

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The input image whose red channel defines a mask. If the red channel pixel value is greater than 0.5 then the point is considered in the mask and output pixel will be zero. Otherwise the output pixel will be a value between zero and one.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var inputImage: CIImage? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidistancegradientfromredmask/inputimage)*