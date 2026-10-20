# continueActivity(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Continues to perform the task for a user activity object using a different block.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func continueActivity(_ block: () -> Void)
```

```objc
- (void) continueActivityUsingBlock:(void (^)()) block;
```

#### Discussion

When AppKit calls [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md) recursively, it may execute this method with the specified block to avoid a deadlock.

If a block that was passed to [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md) is being invoked, this method invokes the passed-in block, having recorded state that makes inner invocations of [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md) not wait. If this method is invoked outside of an invocation of a block passed to [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md), this method simply invokes the passed-in block.

This method is useful when code executed in a block passed to [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md) may also invoke that method. For example, [`save(withDelegate:didSave:contextInfo:)`](./save%28withdelegate,didsave,contextinfo%29.md), which uses [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md), uses this around its invocation of [`runModalSavePanel(for:delegate:didSave:contextInfo:)`](./runmodalsavepanel%28for,delegate,didsave,contextinfo%29.md) or [`save(to:ofType:for:delegate:didSave:contextInfo:)`](./save%28to,oftype,for,delegate,didsave,contextinfo%29.md) because both of those methods also use [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md). Without the use of this method the inner invocation of [`performActivity(withSynchronousWaiting:using:)`](./performactivity%28withsynchronouswaiting,using%29.md) would wait forever.

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
- [func continueAsynchronousWorkOnMainThread(() -> Void)](./continueasynchronousworkonmainthread%28_%29.md)
  Invokes the passed-in block on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/continueactivity(_:))*