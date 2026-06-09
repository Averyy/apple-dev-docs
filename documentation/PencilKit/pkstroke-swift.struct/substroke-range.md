# substroke(range:)

**Framework**: PencilKit  
**Kind**: method

Returns a copy of this stroke containing the control points in the given range.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func substroke(range: ClosedRange<CGFloat>) -> PKStroke
```

## Mentions

- [Controlling stroke rendering for animation and editing](controlling-stroke-rendering-for-animation-and-editing.md)

#### Return Value

A new stroke containing only the control points within the specified range.

#### Discussion

Maintains information for PencilKit rendering to make the copied part of the stroke render the same as the receiver. The returned stroke may have a `renderState` set to maintain this information.

## Parameters

- `range`: The range of control points in the receiver to copy to the returned stroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/substroke(range:))*