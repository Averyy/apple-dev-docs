# decodeReturnType()

**Framework**: Distributed  
**Kind**: method  
**Role**: Instance Method

Attempt to decode the known return type of the distributed invocation.

> **Deprecated**: Not called by 'executeDistributedTarget' anymore, simply return nil

## Declaration

```swift
@export(implementation)
mutating func decodeReturnType() throws -> (any Any.Type)?
```

## Discussion

It is legal to implement this by returning `nil`, and then the system will take the concrete return type from the located function signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder/decodereturntype()-4zo48)*