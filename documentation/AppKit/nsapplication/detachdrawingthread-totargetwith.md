# detachDrawingThread(_:toTarget:with:)

**Framework**: AppKit  
**Kind**: method

Creates and executes a new thread based on the specified target and selector.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class func detachDrawingThread(_ selector: Selector, toTarget target: Any, with argument: Any?)
```

#### Discussion

This method is a convenience wrapper for the [`detachNewThreadSelector(_:toTarget:with:)`](https://developer.apple.com/documentation/foundation/thread/1415633-detachnewthreadselector) method of [`Thread`](https://developer.apple.com/documentation/Foundation/Thread). This method automatically creates an `@autoreleasepool` block for the new thread before invoking `selector`.

## Parameters

- `selector`: The selector whose code you want to execute in the new thread.
- `target`: The object that defines the specified selector.
- `argument`: An optional argument you want to pass to the selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/detachdrawingthread(_:totarget:with:))*