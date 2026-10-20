# performAsynchronousFileAccess(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Waits for any scheduled file access to complete but without blocking the main thread, then invokes the passed-in block.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
func performAsynchronousFileAccess(_ block: @escaping (@escaping () -> Void) -> Void)
```

```objc
- (void) performAsynchronousFileAccessUsingBlock:(void (^)(void (^fileAccessCompletionHandler)())) block;
```

#### Discussion

This method does the same sort of work as [`performSynchronousFileAccess(_:)`](./performsynchronousfileaccess%28_%29.md), but without ever blocking the main thread, and may not invoke the block until after the method invocation has returned, though still always on the same thread as the method invocation. The block is passed another block, the file access completion handler, which must be invoked when the file access is complete, though it can be invoked from any thread. This method is for use with file access that might begin on one thread but continue on another before it is complete. For example, [`save(to:ofType:for:completionHandler:)`](./save%28to,oftype,for,completionhandler%29.md) uses this method instead of [`performSynchronousFileAccess(_:)`](./performsynchronousfileaccess%28_%29.md) because if it does asynchronous saving then there is no way for it to complete all of its file access before returning from the file access block.

## Parameters

- `block`: A block that performs file access.

## See Also

### Performing Tasks Serially
- [func performSynchronousFileAccess(() -> Void)](./performsynchronousfileaccess%28_%29.md)
  Waits for any scheduled file access to complete, then invokes the passed-in block.
- [func performActivity(withSynchronousWaiting: Bool, using: (() -> Void) -> Void)](./performactivity%28withsynchronouswaiting,using%29.md)
  Waits for any work scheduled by previous invocations of this method to complete, then invokes the passed-in block.
- [func continueActivity(() -> Void)](./continueactivity%28_%29.md)
  Continues to perform the task for a user activity object using a different block.
- [func continueAsynchronousWorkOnMainThread(() -> Void)](./continueasynchronousworkonmainthread%28_%29.md)
  Invokes the passed-in block on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/performasynchronousfileaccess(_:))*