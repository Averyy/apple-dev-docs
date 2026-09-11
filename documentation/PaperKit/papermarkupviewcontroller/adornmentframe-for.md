# adornmentFrame(for:)

**Framework**: PaperKit  
**Kind**: method

Returns the current frame of the specified adornment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func adornmentFrame(for id: UUID) -> CGRect?
```

#### Return Value

The frame of the adornment in the coordinate system of this view controller’s view, or `nil` if the canvas does not display the adornment or cannot determine its frame.

#### Discussion

This method calculates the visual frame of an adornment based on its anchor position, image size, attachment point, zoom scale and content offset.

## Parameters

- `id`: The ID of the `MarkupAdornment` whose frame you want to retrieve.

## See Also

- [var adornments: [MarkupAdornment]](papermarkupviewcontroller/adornments.md)
  An array of visual adornments that appear on the markup canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/adornmentframe(for:))*