# present(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Presents a drawable as early as possible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func present(_ drawable: any MTLDrawable)
```

#### Discussion

This convenience method calls the drawable’s [`present()`](mtldrawable/present().md) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [`addScheduledHandler(_:)`](mtlcommandbuffer/addscheduledhandler(_:).md) method for you.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method.

## Parameters

- `drawable`: An   instance that contains a texture the system can show on a display.

## See Also

- [func present(any MTLDrawable, atTime: CFTimeInterval)](mtlcommandbuffer/present(_:attime:).md)
  Presents a drawable at a specific time.
- [func present(any MTLDrawable, afterMinimumDuration: CFTimeInterval)](mtlcommandbuffer/present(_:afterminimumduration:).md)
  Presents a drawable after the system presents the previous drawable for an amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:))*