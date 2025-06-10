# unownedExecutor

**Framework**: IdentityDocumentServices  
**Kind**: property

Retrieve the executor for this actor as an optimized, unowned reference.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
nonisolated
final var unownedExecutor: UnownedSerialExecutor { get }
```

#### Discussion

This property must always evaluate to the same executor for a given actor instance, and holding on to the actor must keep the executor alive.

The system implicitly accesses this property when it needs to schedule work onto this actor. These accesses may be merged, eliminated, and rearranged with other work, and they may even be introduced when not strictly required by the system. Visible side effects are therefore strongly discouraged within this property.

> **Note**:  `SerialExecutor`

> **Note**:  `TaskExecutor`


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/unownedexecutor)*