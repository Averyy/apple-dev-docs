# scope(_:)

**Framework**: Assignables  
**Kind**: method

Sets the user identity for document-related operations that occur within the closure passed in.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@discardableResult
func scope<R>(_ access: () throws -> R) rethrows -> R
```

#### Return Value

The result of the closure.

## Parameters

- `access`: A closure containing   document-related operations . Operations in   the closure will be attributed to this user identity.

## See Also

- [func scope<R>(() async throws -> R) async rethrows -> R](useridentity/scope(_:)-j2jq.md)
  Sets the user identity for document-related operations that occur within the async closure passed in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/useridentity/scope(_:)-esta)*