# init(_:item:subject:message:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init(_ titleKey: LocalizedStringKey, item: URL, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<URL>
```

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is `Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and `Data.Element` conforms to `Transferable`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, item: String, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<String>
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, item: URL, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<URL>
```

```swift
nonisolated
init(_ title: Text, item: String, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<String>
```

```swift
nonisolated
init(_ title: Text, item: URL, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<URL>
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, item: String, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<String>
```

```swift
nonisolated
init<S>(_ title: S, item: String, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<String>, S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, item: URL, subject: Text? = nil, message: Text? = nil) where Data == CollectionOfOne<URL>, S : StringProtocol
```

## Parameters

- `titleKey`: A key identifying the title of the share action.
- `item`: The item to share.
- `subject`: A title for the item to show when sharing to activities that support a subject field.
- `message`: A description of the item to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(_:item:subject:message:)-4czuk)*