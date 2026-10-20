# transform

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The color transform used to initialize the threshold filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var transform: UnsafePointer<Float> { get }
```

```objc
@property (nonatomic, readonly, nonnull) const float * transform;
```

## See Also

### Properties
- [var thresholdValue: Float](./thresholdvalue.md)
  The threshold value used to initialize the threshold filter.
- [var maximumValue: Float](./maximumvalue.md)
  The maximum value used to initialize the threshold filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary/transform)*