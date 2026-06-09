# substroke(with:)

**Framework**: PencilKit  
**Kind**: method

Returns a copy of the stroke containing the control points in the specified range.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func substroke(with range: __PKFloatRange) -> PKStroke
```

#### Return Value

A new stroke containing only the control points within the specified range.

#### Discussion

Maintains rendering information so the returned substroke renders the same as the corresponding portion of the receiver. The returned stroke may have a `renderState` set to maintain this information.

## Parameters

- `range`: The range of control points in the receiver to copy to the returned stroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/substroke(with:))*