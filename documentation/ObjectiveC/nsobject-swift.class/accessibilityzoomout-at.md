# accessibilityZoomOut(at:)

**Framework**: Objective-C Runtime  
**Kind**: method

Zooms out from the content at the specified point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityZoomOut(at point: CGPoint) -> Bool
```

#### Return Value

[`YES`](yes.md) if this method successfully handles zooming; otherwise, [`NO`](no.md). By default, this method returns [`NO`](no.md).

#### Discussion

If your element has the [`supportsZoom`](https://developer.apple.com/documentation/UIKit/UIAccessibilityTraits/supportsZoom) trait, you need to implement this method and [`accessibilityZoomIn(at:)`](nsobject-swift.class/accessibilityzoomin(at:).md). Use this method to zoom out from the specified point. For example, if the element allows a pinch gesture to zoom out from the view’s content, implement this method so that the VoiceOver zoom action receives the same behavior.

## Parameters

- `point`: The point where a person performs the zoom out action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityzoomout(at:))*