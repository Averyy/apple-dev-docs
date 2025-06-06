# GroupActivitySharingResult

**Framework**: Group Activities  
**Kind**: enum

The result of a request to share a group activity in macOS.

**Availability**:
- macOS 13.0+

## Declaration

```swift
enum GroupActivitySharingResult
```

## Topics

### Operators
- [static func == (GroupActivitySharingResult, GroupActivitySharingResult) -> Bool](groupactivitysharingresult-1gln2/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [GroupActivitySharingResult.cancelled](groupactivitysharingresult-1gln2/cancelled.md)
  A result that indicates the user canceled the request.
- [GroupActivitySharingResult.success](groupactivitysharingresult-1gln2/success.md)
  A result that indicates the user wants to share the activity with the group.
### Instance Properties
- [var hashValue: Int](groupactivitysharingresult-1gln2/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](groupactivitysharingresult-1gln2/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](groupactivitysharingresult-1gln2/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var result: GroupActivitySharingResult](groupactivitysharingcontroller-4gtfk/result.md)
  The result of a request to share a group activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitysharingresult-1gln2)*