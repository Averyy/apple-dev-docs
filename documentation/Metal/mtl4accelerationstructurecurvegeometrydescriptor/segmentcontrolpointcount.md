# segmentControlPointCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Declares the number of control points per curve segment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var segmentControlPointCount: Int { get set }
```

```objc
@property (nonatomic) NSUInteger segmentControlPointCount;
```

#### Discussion

Valid values for this property are `2`, `3`, or `4`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/segmentcontrolpointcount)*