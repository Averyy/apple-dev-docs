# present(_:atTime:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Presents a drawable at a specific time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func present(_ drawable: any MTLDrawable, atTime presentationTime: CFTimeInterval)
```

```objc
- (void) presentDrawable:(id<MTLDrawable>) drawable atTime:(CFTimeInterval) presentationTime;
```

## Discussion

This convenience method calls the drawable’s [`present(at:)`](../mtldrawable/present%28at%29.md) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [`addScheduledHandler(_:)`](./addscheduledhandler%28_%29.md) method for you.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](./commit%28%29.md) method.

## Parameters

- `drawable`: An [`MTLDrawable`](../mtldrawable.md) instance that contains a texture the system can show on a display.
- `presentationTime`: The Mach absolute time, in seconds, that you want to present the drawable.

## See Also

### Presenting a drawable
- [func present(any MTLDrawable)](./present%28_%29.md)
  Presents a drawable as early as possible.
- [func present(any MTLDrawable, afterMinimumDuration: CFTimeInterval)](./present%28_,afterminimumduration%29.md)
  Presents a drawable after the system presents the previous drawable for an amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:attime:))*