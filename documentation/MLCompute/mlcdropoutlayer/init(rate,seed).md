# init(rate:seed:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a dropout layer with the probability rate and random number generator seed you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(rate: Float, seed: Int)
```

```objc
+ (instancetype) layerWithRate:(float) rate seed:(NSUInteger) seed;
```

## Parameters

- `rate`: The dropout rate you use for each element.
- `seed`: The seed you use to generate random numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdropoutlayer/init(rate:seed:))*