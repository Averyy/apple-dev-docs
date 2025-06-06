# present(_:atTime:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Presents a drawable at a specific time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func present(_ drawable: any MTLDrawable, atTime presentationTime: CFTimeInterval)
```

#### Discussion

This convenience method calls the drawable’s [`present(at:)`](mtldrawable/present(at:).md) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [`addScheduledHandler(_:)`](mtlcommandbuffer/addscheduledhandler(_:).md) method for you.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method.

 You can only call this method before calling the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method.

## Parameters

- `drawable`: An   instance that contains a texture the system can show on a display.
- `presentationTime`: The Mach absolute time, in seconds, that you want to present the drawable.

## See Also

- [func present(any MTLDrawable)](mtlcommandbuffer/present(_:).md)
  Presents a drawable as early as possible.
- [func present(any MTLDrawable, afterMinimumDuration: CFTimeInterval)](mtlcommandbuffer/present(_:afterminimumduration:).md)
  Presents a drawable after the system presents the previous drawable for an amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:attime:))*