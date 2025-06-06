# init(fromSplitComplex:scale:count:)

**Framework**: Swift  
**Kind**: init

Creates a new array of single-precision values from a `DSPSplitComplex` structure.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(fromSplitComplex splitComplex: DSPSplitComplex, scale: Float, count: Int)
```

## Parameters

- `scale`: A multiplier to apply during conversion.
- `count`: The length of the required resulting array (typically half the count of either the real or imaginary parts of the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/init(fromsplitcomplex:scale:count:)-5eirc)*