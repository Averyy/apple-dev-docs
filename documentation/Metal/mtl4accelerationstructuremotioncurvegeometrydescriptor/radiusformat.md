# radiusFormat

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Sets the format of the radii in the radius buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var radiusFormat: MTLAttributeFormat { get set }
```

```objc
@property (nonatomic) MTLAttributeFormat radiusFormat;
```

#### Discussion

Defaults to  `MTLAttributeFormatFloat`. All keyframes share the same radius format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/radiusformat)*