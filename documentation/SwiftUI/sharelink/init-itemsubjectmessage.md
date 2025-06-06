# init(_:item:subject:message:)

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
init(_ title: Text, item: String, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<String>
```

## Parameters

- `title`: The title of the share action.
- `item`: The item to share.
- `subject`: A title for the item to show when sharing to activities   that support a subject field.
- `message`: A description of the item to show when sharing to   activities that support a message field. Activities may   support attributed text or HTML strings.

## See Also

- [init(item:subject:message:)](sharelink/init(item:subject:message:).md)
  Creates an instance that presents the share interface.
- [init(item:subject:message:label:)](sharelink/init(item:subject:message:label:).md)
  Creates an instance that presents the share interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(_:item:subject:message:))*