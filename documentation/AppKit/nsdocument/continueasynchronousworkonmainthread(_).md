# continueAsynchronousWorkOnMainThread(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invokes the passed-in block on the main thread.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
func continueAsynchronousWorkOnMainThread(_ block: @escaping () -> Void)
```

```objc
- (void) continueAsynchronousWorkOnMainThreadUsingBlock:(void (^)()) block;
```

#### Discussion

If the main thread is blocked by an invocation of [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md) or [`performSynchronousFileAccess(_:)`](./performsynchronousfileaccess%28_%29.md), this method interrupts that blocking activity, performs the specified `block`, and then resumes the blocking activity after `block` returns. Invocations of this method always return before the passed-in block is invoked.

You can invoke this method when work is being done on a non-main thread and part of the work must be continued on the main thread. For example, [`save(to:ofType:for:completionHandler:)`](./save%28to,oftype,for,completionhandler%29.md) uses this method when it has just completed the actual writing of the file during asynchronous saving and, to finish the saving operation, must invoke [`updateChangeCount(withToken:for:)`](./updatechangecount%28withtoken,for%29.md) and other methods on the main thread.

This method can be invoked on any thread.

## Parameters

- `block`: The block to be invoked.

## See Also

### Performing Tasks Serially
- [func performSynchronousFileAccess(() -> Void)](./performsynchronousfileaccess%28_%29.md)
  Waits for any scheduled file access to complete, then invokes the passed-in block.
- [func performAsynchronousFileAccess((() -> Void) -> Void)](./performasynchronousfileaccess%28_%29.md)
  Waits for any scheduled file access to complete but without blocking the main thread, then invokes the passed-in block.
- [func performActivity(withSynchronousWaiting: Bool, using: (() -> Void) -> Void)](./performactivity%28withsynchronouswaiting,using%29.md)
  Waits for any work scheduled by previous invocations of this method to complete, then invokes the passed-in block.
- [func continueActivity(() -> Void)](./continueactivity%28_%29.md)
  Continues to perform the task for a user activity object using a different block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/continueasynchronousworkonmainthread(_:))*