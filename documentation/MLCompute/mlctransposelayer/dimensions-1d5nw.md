# dimensions

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains an input axis source for each output axis, which represents the ordering of dimensions.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<NSNumber *> * dimensions;
```

#### Discussion

Permutes the dimensions according to `dimensions`. The returned tensor’s dimension `i` corresponds to `dimensions[i]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctransposelayer/dimensions-1d5nw)*