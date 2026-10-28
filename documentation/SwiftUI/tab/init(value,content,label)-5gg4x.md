# init(value:content:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new tab with a label that you can use in a tab view.

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
init<V>(value: V, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label) where Value == V?, V : Hashable
```

Available when `Value` conforms to `Hashable`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(value: Value, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `value`: The `selection` value which selects this tab.
- `content`: The view content of the tab.
- `label`: The label for the tab’s tab item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(value:content:label:)-5gg4x)*