# extentAtDimensionIndex:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Returns the value at the specified dimension index.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (NSInteger) extentAtDimensionIndex:(NSUInteger) dimensionIndex;
```

#### Return Value

The value at `dimensionIndex`, or `-1` if `dimensionIndex` is greater than or equal to [`rank`](./rank.md).

## Parameters

- `dimensionIndex`: The index of the value to retrieve. The first index corresponds to the innermost dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorextents/extentatdimensionindex:)*