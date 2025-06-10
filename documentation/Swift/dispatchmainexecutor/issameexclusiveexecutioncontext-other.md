# isSameExclusiveExecutionContext(other:)

**Framework**: Swift  
**Kind**: method

If this executor has complex equality semantics, and the runtime needs to compare two executors, it will first attempt the usual pointer-based equality / check, / and if it fails it will compare the types of both executors, if they are the same, / it will finally invoke this method, in an attempt to let the executor itself decide / if this and the `other` executor represent the same serial, exclusive, isolation context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func isSameExclusiveExecutionContext(other: Self) -> Bool
```

#### Return Value

`true`, if `self` and the `other` executor actually are mutually exclusive and it is safe–from a concurrency perspective–to execute code assuming one on the other.

#### Discussion

This method must be implemented with great care, as wrongly returning `true` would allow / code from a different execution context (e.g. thread) to execute code which was intended to be isolated by another actor.

This check is not used when performing executor switching.

This check is used when performing `Actor/assertIsolated()`, `Actor/preconditionIsolated()`, `Actor/assumeIsolated()` and similar APIs which assert about the same “exclusive serial execution context”.

## Parameters

- `other`: The executor to compare with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dispatchmainexecutor/issameexclusiveexecutioncontext(other:))*