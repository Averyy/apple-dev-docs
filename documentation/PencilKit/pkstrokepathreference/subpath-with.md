# subpath(with:)

**Framework**: PencilKit  
**Kind**: method

Returns a copy of the path containing the control points in the specified parametric range.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func subpath(with range: __PKFloatRange) -> PKStrokePath
```

#### Return Value

A new stroke path containing the portion within the specified parametric range.

## Parameters

- `range`: The parametric range to copy. Values must be within [0, count-1].


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/subpath(with:))*