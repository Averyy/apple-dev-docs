# frame(forAdornmentWithID:)

**Framework**: PaperKit  
**Kind**: method

Returns the current frame of the specified adornment.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func frame(forAdornmentWithID adornmentID: UUID) -> CGRect?
```

#### Return Value

The frame of the adornment in the coordinate system of this view controller’s view, or `nil` if the canvas does not display the adornment or cannot determine its frame.

#### Discussion

This method calculates the visual frame of an adornment based on its anchor position, image size, attachment point, zoom scale and content offset.

## Parameters

- `adornmentID`: The ID of the `MarkupAdornment` whose frame you want to retrieve.

## See Also

- [var adornments: [MarkupAdornment]](papermarkupviewcontroller/adornments.md)
  An array of visual adornments that appear on the markup canvas.
- [func adornmentFrame(for: UUID) -> CGRect?](papermarkupviewcontroller/adornmentframe(for:).md)
  Returns the current frame of the specified adornment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/frame(foradornmentwithid:))*