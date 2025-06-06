# dimensions

**Framework**: ML Compute  
**Kind**: property

An array that contains an input axis source for each output axis, which represents the ordering of dimensions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var dimensions: [Int] { get }
```

#### Discussion

Permutes the dimensions according to `dimensions`. The returned tensor’s dimension `i` corresponds to `dimensions[i]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctransposelayer/dimensions-71ed6)*