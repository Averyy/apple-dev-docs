# includeZeroPadToAverage

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

Defines a mode for average pooling, where samples outside the input tensor count as zeroes in the average computation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var includeZeroPadToAverage: Bool { get set }
```

#### Discussion

Otherwise the result is sum over samples divided by number of samples that didn’t come from padding. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/includezeropadtoaverage)*