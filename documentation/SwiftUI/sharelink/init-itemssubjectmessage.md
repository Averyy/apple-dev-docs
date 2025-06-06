# init(_:items:subject:message:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance, with a custom label, that presents the share interface.

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
init(_ title: Text, items: Data, subject: Text? = nil, message: Text? = nil)
```

## Parameters

- `title`: The title of the share action.
- `items`: The items to share.
- `subject`: A title for the items to show when sharing to activities   that support a subject field.
- `message`: A description of the items to show when sharing to   activities that support a message field. Activities may   support attributed text or HTML strings.

## See Also

- [init(items:subject:message:)](sharelink/init(items:subject:message:).md)
  Creates an instance that presents the share interface.
- [init(items:subject:message:label:)](sharelink/init(items:subject:message:label:).md)
  Creates an instance that presents the share interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(_:items:subject:message:))*