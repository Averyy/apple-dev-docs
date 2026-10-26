# present(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Presents a texture resource drawable as early as possible.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
func present(_ drawable: TextureResource.Drawable)
```

#### Discussion

This convenience method calls the drawable’s [`present()`](../mtldrawable/present%28%29.md) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [`addScheduledHandler(_:)`](./addscheduledhandler%28_%29.md) method for you.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](./commit%28%29.md) method.

## Parameters

- `drawable`: A [`TextureResource.Drawable`](../../RealityKit/textureresource/drawable.md) instance that contains a texture the system can show on a display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:)-8nfpq)*