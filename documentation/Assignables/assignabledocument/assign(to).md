# assign(to:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Assign this document to a user.

**Availability**:
- iOS 17.4+ - Deprecated in 18.0
- iPadOS 17.4+ - Deprecated in 18.0
- Mac Catalyst 17.4+ - Deprecated in 18.0
- visionOS

> **Deprecated**: Use makeAssignedWorkDocument() instead

## Declaration

```swift
func assign(to userIdentity: AnyUserIdentity) throws -> AssignedWorkDocument
```

#### Return Value

A work document for the taker of the assignable document.

## Parameters

- `userIdentity`: The identity of the user to assign this document to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/assign(to:))*