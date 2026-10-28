# assign(to:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assign this document to a user.

**Availability**:
- iOS 17.4+ - Deprecated in 18.0
- iPadOS 17.4+ - Deprecated in 18.0
- Mac Catalyst 17.4+ - Deprecated in 18.0
- visionOS

> **Deprecated**: Use makeAssignedWorkDocument() instead

## Declaration

```swift
func assign(to userIdentity: some UserIdentity) throws -> AssignedWorkDocument
```

## Return Value

A work document for the taker of the assignable document.

## Parameters

- `userIdentity`: The identity of the user to assign this document to.

## Default Implementations

### Assignable Implementations
- [func assign(to: some UserIdentity) throws -> AssignedWorkDocument](./assign%28to%29-629jq.md)
  Assign this document to a user.

## See Also

### Assigning a document
- [func assign(to: AnyUserIdentity) throws -> AssignedWorkDocument](./assign%28to%29-4jnsl.md)
  Assign this document to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignable/assign(to:)-4mit8)*