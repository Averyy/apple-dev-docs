# init(_:items:subject:message:)

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
init(_ titleKey: LocalizedStringKey, items: Data, subject: Text? = nil, message: Text? = nil)
```

Available when `Data` conforms to `RandomAccessCollection`, `PreviewImage` is `Never`, `PreviewIcon` is `Never`, `Label` is `DefaultShareLinkLabel`, and `Data.Element` is `URL`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, items: Data, subject: Text? = nil, message: Text? = nil)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, items: Data, subject: Text? = nil, message: Text? = nil)
```

```swift
nonisolated
init(_ title: Text, items: Data, subject: Text? = nil, message: Text? = nil)
```

```swift
nonisolated
init(_ title: Text, items: Data, subject: Text? = nil, message: Text? = nil)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, items: Data, subject: Text? = nil, message: Text? = nil)
```

```swift
nonisolated
init<S>(_ title: S, items: Data, subject: Text? = nil, message: Text? = nil) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, items: Data, subject: Text? = nil, message: Text? = nil) where S : StringProtocol
```

## Parameters

- `titleKey`: A key identifying the title of the share action.
- `items`: The items to share.
- `subject`: A title for the items to show when sharing to activities that support a subject field.
- `message`: A description of the items to show when sharing to activities that support a message field. Activities may support attributed text or HTML strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharelink/init(_:items:subject:message:)-9fwh5)*