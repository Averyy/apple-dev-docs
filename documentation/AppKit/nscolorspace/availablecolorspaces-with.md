# availableColorSpaces(with:)

**Framework**: AppKit  
**Kind**: method

Returns the list of color spaces available on the system that are displayed in the color panel, in the order they are displayed in the color panel.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func availableColorSpaces(with model: NSColorSpace.Model) -> [NSColorSpace]
```

#### Return Value

The list of color spaces, or an empty array if no color spaces are available for the specified model.

#### Discussion

This method doesn’t return color spaces created on the fly or spaces without user-displayable names. Pass [`NSUnknownColorSpaceModel`](nsunknowncolorspacemodel.md) as `model` to get all available color spaces.

## Parameters

- `model`: The model to return the color spaces for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/availablecolorspaces(with:))*