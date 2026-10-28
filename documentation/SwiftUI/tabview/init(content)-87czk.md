# init(content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a tab view that uses a builder to create its tabs.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init<C>(@TabContentBuilder<Never> content: () -> C) where SelectionValue == Never, Content == TabContentBuilder<Never>.Content<C>, C : TabContent
```

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content`: The [`Tab`](../tab.md) content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabview/init(content:)-87czk)*