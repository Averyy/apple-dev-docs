# init(item:subject:message:)

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
init(item: URL, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<URL>
```

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is `Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

**Other overloads**:

```swift
nonisolated
init(item: String, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<String>
```

## Discussion

Use this initializer when you want the system-standard appearance for `ShareLink`.

## Parameters

- `item`: The item to share.
- `subject`: A title for the item to show when sharing to activities that support a subject field.
- `message`: A description of the item to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(item:subject:message:)-9ap6z)*