# present(_:afterMinimumDuration:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Presents a drawable after the system presents the previous drawable for an amount of time.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func present(_ drawable: any MTLDrawable, afterMinimumDuration duration: CFTimeInterval)
```

#### Discussion

This convenience method calls the drawable’s [`present(afterMinimumDuration:)`](mtldrawable/present(afterminimumduration:).md) method after the command queue schedules the command buffer for execution. The command buffer does this by adding a completion handler by calling its own [`addScheduledHandler(_:)`](mtlcommandbuffer/addscheduledhandler(_:).md) method for you.

> ❗ **Important**:  You can only call this method before calling the command buffer’s [`commit()`](mtlcommandbuffer/commit().md) method.

## Parameters

- `drawable`: An   instance that contains a texture the system can show on a display.
- `duration`: The shortest display time you want the system to give to the previous drawable before presenting this one.

## See Also

- [func present(any MTLDrawable)](mtlcommandbuffer/present(_:).md)
  Presents a drawable as early as possible.
- [func present(any MTLDrawable, atTime: CFTimeInterval)](mtlcommandbuffer/present(_:attime:).md)
  Presents a drawable at a specific time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:afterminimumduration:))*