# init(items:subject:message:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that presents the share interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(items: Data, subject: Text? = nil, message: Text? = nil, @ViewBuilder label: () -> Label)
```

## Parameters

- `items`: The items to share.
- `subject`: A title for the items to show when sharing to activities   that support a subject field.
- `message`: A description of the items to show when sharing to   activities that support a message field. Activities may   support attributed text or HTML strings.
- `label`: A view builder that produces a label that describes the   share action.

## See Also

- [init(items:subject:message:)](sharelink/init(items:subject:message:).md)
  Creates an instance that presents the share interface.
- [init(_:items:subject:message:)](sharelink/init(_:items:subject:message:).md)
  Creates an instance, with a custom label, that presents the share interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(items:subject:message:label:))*