# relative(to:)

**Framework**: Core AI  
**Kind**: method  
**Required**: Yes

Returns Range for the dimension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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