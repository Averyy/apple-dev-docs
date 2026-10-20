# present(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Presents a drawable as early as possible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func present(_ drawable: any MTLDrawable)
```

```objc
- (void) presentDrawable:(id<MTLDrawable>) drawable;
```

#### Discussion

This convenience method calls the drawable’s [`present()`](../mtldrawable/present%28%29.md) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [`addScheduledHandler(_:)`](./addscheduledhandler%28_%29.md) method for you.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](./commit%28%29.md) method.

## Parameters

- `drawable`: An [`MTLDrawable`](../mtldrawable.md) instance that contains a texture the system can show on a display.

## Default Implementations

### MTLCommandBuffer Implementations
- [func present(TextureResource.Drawable)](./present%28_%29-8nfpq.md)
  Presents a texture resource drawable as early as possible.

## See Also

### Presenting a drawable
- [func present(any MTLDrawable, atTime: CFTimeInterval)](./present%28_,attime%29.md)
  Presents a drawable at a specific time.
- [func present(any MTLDrawable, afterMinimumDuration: CFTimeInterval)](./present%28_,afterminimumduration%29.md)
  Presents a drawable after the system presents the previous drawable for an amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:))*