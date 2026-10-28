# dilationRates

**Framework**: Metal Performance Shaders Graph  
**Kind**: property  
**Role**: Instance Property

The dilation rates for spatial dimensions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var dilationRates: [NSNumber] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSArray<NSNumber *> * dilationRates;
```

## Discussion

Must be three numbers, one for each spatial dimension, fastest running index last. Default value: `@[ @1, @1, @1 ]`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdepthwiseconvolution3dopdescriptor/dilationrates)*