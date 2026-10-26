# decodeErrorType()

**Framework**: Distributed  
**Kind**: method  
**Role**: Instance Method

Decode the specific error type that the distributed invocation target has recorded. Currently this effectively can only ever be `Error.self`.

> **Deprecated**: Not called by 'executeDistributedTarget' anymore, simply return nil

## Declaration

```swift
@export(implementation)
mutating func decodeErrorType() throws -> (any Any.Type)?
```

#### Discussion

If the target known to not be throwing, or no error type was recorded, the method should return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder/decodeerrortype()-2ey6c)*