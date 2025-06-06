# ExecuteDistributedTargetError.ErrorCode

**Framework**: Distributed  
**Kind**: enum

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum ErrorCode
```

## Topics

### Operators
- [static func == (ExecuteDistributedTargetError.ErrorCode, ExecuteDistributedTargetError.ErrorCode) -> Bool](executedistributedtargeterror/errorcode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ExecuteDistributedTargetError.ErrorCode.invalidGenericSubstitutions](executedistributedtargeterror/errorcode-swift.enum/invalidgenericsubstitutions.md)
  Generic substitutions provided by invocation decoder are incompatible with target of the call. E.g. the generic requirements on the actual target could not be fulfilled by the obtained generic substitutions.
- [ExecuteDistributedTargetError.ErrorCode.invalidParameterCount](executedistributedtargeterror/errorcode-swift.enum/invalidparametercount.md)
  Call target has different number of parameters than arguments provided by the invocation decoder.
- [ExecuteDistributedTargetError.ErrorCode.missingGenericSubstitutions](executedistributedtargeterror/errorcode-swift.enum/missinggenericsubstitutions.md)
  Target expects generic environment information, but invocation decoder provided no generic substitutions.
- [ExecuteDistributedTargetError.ErrorCode.other](executedistributedtargeterror/errorcode-swift.enum/other.md)
  A general issue during the execution of the distributed call target occurred.
- [ExecuteDistributedTargetError.ErrorCode.targetAccessorNotFound](executedistributedtargeterror/errorcode-swift.enum/targetaccessornotfound.md)
  Unable to resolve the target identifier to a function accessor. This can happen when the identifier is corrupt, illegal, or wrong in the sense that the caller and callee do not have the called function recorded using the same identifier.
- [ExecuteDistributedTargetError.ErrorCode.typeDeserializationFailure](executedistributedtargeterror/errorcode-swift.enum/typedeserializationfailure.md)
### Instance Properties
- [var hashValue: Int](executedistributedtargeterror/errorcode-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](executedistributedtargeterror/errorcode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](executedistributedtargeterror/errorcode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/executedistributedtargeterror/errorcode-swift.enum)*