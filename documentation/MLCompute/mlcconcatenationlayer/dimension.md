# dimension

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The dimension, or axis, along which you concatenate tensors.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var dimension: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger dimension;
```

#### Discussion

The default value is `1`, which typically represents features channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconcatenationlayer/dimension)*