# continueActivity(_:)

**Framework**: AppKit  
**Kind**: method

Continues to perform the task for a user activity object using a different block.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func continueActivity(_ block: () -> Void)
```

#### Discussion

When AppKit calls [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md) recursively, it may execute this method with the specified block to avoid a deadlock.

If a block that was passed to [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md) is being invoked, this method invokes the passed-in block, having recorded state that makes inner invocations of [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md) not wait. If this method is invoked outside of an invocation of a block passed to [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md), this method simply invokes the passed-in block.

This method is useful when code executed in a block passed to [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md) may also invoke that method. For example, [`save(withDelegate:didSave:contextInfo:)`](nsdocument/save(withdelegate:didsave:contextinfo:).md), which uses [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md), uses this around its invocation of [`runModalSavePanel(for:delegate:didSave:contextInfo:)`](nsdocument/runmodalsavepanel(for:delegate:didsave:contextinfo:).md) or [`save(to:ofType:for:delegate:didSave:contextInfo:)`](nsdocument/save(to:oftype:for:delegate:didsave:contextinfo:).md) because both of those methods also use [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md). Without the use of this method the inner invocation of [`performActivity(withSynchronousWaiting:using:)`](nsdocument/performactivity(withsynchronouswaiting:using:).md) would wait forever.

## Parameters

- `block`: The block to be invoked.

## See Also

- [func performSynchronousFileAccess(() -> Void)](nsdocument/performsynchronousfileaccess(_:).md)
  Waits for any scheduled file access to complete, then invokes the passed-in block.
- [func performAsynchronousFileAccess((() -> Void) -> Void)](nsdocument/performasynchronousfileaccess(_:).md)
  Waits for any scheduled file access to complete but without blocking the main thread, then invokes the passed-in block.
- [func performActivity(withSynchronousWaiting: Bool, using: (() -> Void) -> Void)](nsdocument/performactivity(withsynchronouswaiting:using:).md)
  Waits for any work scheduled by previous invocations of this method to complete, then invokes the passed-in block.
- [func continueAsynchronousWorkOnMainThread(() -> Void)](nsdocument/continueasynchronousworkonmainthread(_:).md)
  Invokes the passed-in block on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/continueactivity(_:))*