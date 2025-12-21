# signalDrawable(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Schedules a signal operation on the command queue to indicate when rendering to a Metal drawable is complete.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func signalDrawable(_ drawable: any MTLDrawable)
```

#### Discussion

Signaling when rendering to a [`MTLDrawable`](mtldrawable.md) instance is complete indicates that it’s safe to present it to the display.

You are responsible for calling this method after committing all command buffers that contain commands targeting this drawable, and before calling [`present()`](mtldrawable/present().md), [`present(at:)`](mtldrawable/present(at:).md), or [`present(afterMinimumDuration:)`](mtldrawable/present(afterminimumduration:).md).

> **Note**: This method doesn’t trigger the presentation of the drawable, and fails if you call it after any of the present methods, or if you call it multiple times.

Metal doesn’t guarantee that command buffers you commit to the command queue after calling this method execute before presentation.

## Parameters

- `drawable`:   instance to signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/signaldrawable(_:))*