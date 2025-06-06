# preconditionIsolated(_:file:line:)

**Framework**: SecureElementCredential  
**Kind**: method

Stops program execution if the current task is not executing on this actor’s serial executor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@backDeployed(before: macOS 14.0, iOS 17.0, watchOS 10.0, tvOS 17.0)
nonisolated func preconditionIsolated(_ message: @autoclosure () -> String = String(), file: StaticString = #fileID, line: UInt = #line)
```

#### Discussion

This function’s effect varies depending on the build flag used:

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration), stops program execution in a debuggable state after printing `message`.
- In `-O` builds (the default for Xcode’s Release configuration), stops program execution.

> **Note**: This check is performed against the actor’s serial executor, meaning that / if another actor uses the same serial executor–by using that actor’s serial executor as its own `Actor/unownedExecutor`–this check will succeed , as from a concurrency safety perspective, the serial executor guarantees mutual exclusion of those two actors.

This check is performed against the actor’s serial executor, meaning that / if another actor uses the same serial executor–by using that actor’s serial executor as its own `Actor/unownedExecutor`–this check will succeed , as from a concurrency safety perspective, the serial executor guarantees mutual exclusion of those two actors.

## Parameters

- `message`: The message to print if the assertion fails.
- `file`: The file name to print if the assertion fails. The default is   where this method was called.
- `line`: The line number to print if the assertion fails The default is   where this method was called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/preconditionisolated(_:file:line:))*