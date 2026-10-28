# init(items:subject:message:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init(items: Data, subject: Text? = nil, message: Text? = nil, @ContentBuilder label: () -> Label)
```

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is `Never`, `PreviewIcon` is `Never`, `Label` conforms to `View`, and `Data.Element` is `String`.

**Other overloads**:

```swift
nonisolated
init(items: Data, subject: Text? = nil, message: Text? = nil, @ContentBuilder label: () -> Label)
```

## Parameters

- `items`: The items to share.
- `subject`: A title for the items to show when sharing to activities that support a subject field.
- `message`: A description of the items to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.
- `label`: A content builder that produces a label that describes the share action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(items:subject:message:label:)-8t9gm)*