# unownedExecutor

**Framework**: Corehid  
**Kind**: property

Retrieve the executor for this actor as an optimized, unowned reference.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 15.0+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
final var unownedExecutor: UnownedSerialExecutor { get }
```

#### Discussion

This property must always evaluate to the same executor for a given actor instance, and holding on to the actor must keep the executor alive.

This property will be implicitly accessed when work needs to be scheduled onto this actor.  These accesses may be merged, eliminated, and rearranged with other work, and they may even be introduced when not strictly required.  Visible side effects are therefore strongly discouraged within this property.

> **Note**: `SerialExecutor`

> **Note**: `TaskExecutor`


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreHID/hiddeviceclient/unownedexecutor)*