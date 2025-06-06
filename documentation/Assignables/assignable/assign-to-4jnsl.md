# assign(to:)

**Framework**: Assignables  
**Kind**: method  
**Required**: Yes

Assign this document to a user.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
func assign(to userIdentity: AnyUserIdentity) throws -> AssignedWorkDocument
```

#### Return Value

A work document for the taker of the assignable document.

## Parameters

- `userIdentity`: The identity of the user to assign this document to.

## See Also

- [func assign(to: some UserIdentity) throws -> AssignedWorkDocument](assignable/assign(to:)-4mit8.md)
  Assign this document to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignable/assign(to:)-4jnsl)*