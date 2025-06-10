# assumeIsolated(_:file:line:)

**Framework**: Core HID  
**Kind**: method

Assume that the current task is executing on this actor’s serial executor, or stop program execution otherwise.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func assumeIsolated<T>(_ operation: (isolated Self) throws -> T, file: StaticString = #fileID, line: UInt = #line) rethrows -> T where T : Sendable
```

#### Return Value

The return value of the `operation`

#### Discussion

You call this method to  that the currently executing synchronous function is actually executing on the serial executor of this actor.

If that is the case, the operation is invoked with an `isolated` version of the actor, allowing synchronous access to actor local state without hopping through asynchronous boundaries.

If the current context is not running on the actor’s serial executor, or if the actor is a reference to a remote actor, this method will crash with a fatal error (similar to `preconditionIsolated()`).

Note that this check is performed against the passed in actor’s serial executor, meaning that if another actor uses the same serial executor–by using that actor’s `Actor/unownedExecutor` as its own `Actor/unownedExecutor`–this check will succeed, as from a concurrency safety perspective, the serial executor guarantees mutual exclusion of those two actors.

This method can only be used from synchronous functions, as asynchronous functions should instead perform a normal method call to the actor, which will hop task execution to the target actor if necessary.

> **Note**: This check is performed against the actor’s serial executor, meaning that / if another actor uses the same serial executor–by using another actor’s executor as its own `Actor/unownedExecutor` –this check will succeed , as from a concurrency safety perspective, the serial executor guarantees mutual exclusion of those two actors.

> **Note**: Rethrows the `Error` thrown by the operation if it threw

## Parameters

- `operation`: The operation that will be executed if the current context   is executing on the actors serial executor.
- `file`: The file name to print if the assertion fails. The default is   where this method was called.
- `line`: The line number to print if the assertion fails The default is   where this method was called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/assumeisolated(_:file:line:))*