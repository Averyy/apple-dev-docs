# assertIsolated(_:file:line:)

**Framework**: Distributed  
**Kind**: method

Stops program execution if the current task is not executing on this actor’s serial executor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func assertIsolated(_ message: @autoclosure () -> String = String(), file: StaticString = #fileID, line: UInt = #line)
```

#### Discussion

This function’s effect varies depending on the build flag used:

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration), stops program execution in a debuggable state after printing `message`.
- In `-O` builds (the default for Xcode’s Release configuration), the isolation check is not performed and there are no effects.

> **Note**: This check is performed against the actor’s serial executor, meaning that / if another actor uses the same serial executor–by using that actor’s serial executor as its own `Actor/unownedExecutor`–this check will succeed , as from a concurrency safety perspective, the serial executor guarantees mutual exclusion of those two actors.

This check is performed against the actor’s serial executor, meaning that / if another actor uses the same serial executor–by using that actor’s serial executor as its own `Actor/unownedExecutor`–this check will succeed , as from a concurrency safety perspective, the serial executor guarantees mutual exclusion of those two actors.

## Parameters

- `message`: The message to print if the assertion fails.
- `file`: The file name to print if the assertion fails. The default is   where this method was called.
- `line`: The line number to print if the assertion fails The default is   where this method was called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/assertisolated(_:file:line:))*