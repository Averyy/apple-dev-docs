# relative(to:)

**Framework**: Core AI  
**Kind**: method  
**Required**: Yes

Returns Range for the dimension.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func relative(to dimension: Range<Int>) -> Range<Int>
```

#### Return Value

The range of the selected dimension.

#### Discussion

For example, when the range expression specifies `1...` on the axis with dimension 3, the resultant Range is `1 ..< 3`.

## Parameters

- `dimension`: The dimension of the axis on which the range expression is used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rangeexpression/relative(to:))*