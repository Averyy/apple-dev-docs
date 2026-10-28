# decodeReturnType()

**Framework**: Distributed  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Attempt to decode the known return type of the distributed invocation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Not called by 'executeDistributedTarget' anymore, simply return nil

## Declaration

```swift
mutating func decodeReturnType() throws -> (any Any.Type)?
```

## Discussion

It is legal to implement this by returning `nil`, and then the system will take the concrete return type from the located function signature.

## Default Implementations

### DistributedTargetInvocationDecoder Implementations
- [func decodeReturnType() throws -> (any Any.Type)?](./decodereturntype%28%29-4zo48.md)
  Attempt to decode the known return type of the distributed invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder/decodereturntype())*