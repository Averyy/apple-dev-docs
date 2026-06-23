# convertInteractionPoint(_:toContainerAt:)

**Framework**: UIKit  
**Kind**: method

Converts an interaction point from display space into the text container’s coordinate system.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
optional func convertInteractionPoint(_ point: CGPoint, toContainerAt containerLocation: any NSTextLocation) -> CGPoint
```

#### Return Value

The point mapped into the text container’s coordinate system. Return `point` unchanged when no transform is active.

#### Discussion

`NSTextSelectionNavigation` calls this method before hit-testing to allow the data source to undo any display transform (rotation, flip, path layout, etc.) applied to the text.

## Parameters

- `point`: The interaction point in display/view-space coordinates.
- `containerLocation`: The location identifying the text container the interaction occurred in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/convertinteractionpoint(_:tocontainerat:))*