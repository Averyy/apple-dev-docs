# ConstraintError

**Framework**: LightweightCodeRequirements  
**Kind**: enum

Error types that can be thrown from lightweight code requirement routines.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
enum ConstraintError
```

## Topics

### Operators
- [static func == (ConstraintError, ConstraintError) -> Bool](constrainterror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ConstraintError.duplicateKey](constrainterror/duplicatekey.md)
  Two constraints of the same type were found in the same logical group.
- [ConstraintError.malformedConstraint](constrainterror/malformedconstraint.md)
  An unexpected type was found when trying to encode or decode a constraint.
- [ConstraintError.taskIsNoLongerValid](constrainterror/taskisnolongervalid.md)
  A SecTask operation failed because the task is no longer valid
- [ConstraintError.unsupportedConstraintForRequirementType](constrainterror/unsupportedconstraintforrequirementtype.md)
  Converting one code requirement type to another failed because the original requirement included a constraint that is not supported by the target requirement type.
### Instance Properties
- [var hashValue: Int](constrainterror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](constrainterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](constrainterror/equatable-implementations.md)
- [Error Implementations](constrainterror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/constrainterror)*