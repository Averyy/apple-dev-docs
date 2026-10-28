# init(value:role:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new tab with a label inferred from the role.

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
init<V>(value: V, role: TabRole?, @ContentBuilder content: () -> Content) where Value == V?, Label == DefaultTabLabel, V : Hashable
```

Available when `Value` conforms to `Hashable`, `Content` conforms to `View`, and `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(value: Value, role: TabRole?, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `value`: The `selection` value which selects this tab.
- `role`: The `role` defining the semantic purpose of the tab.
- `content`: The view content of the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tab/init(value:role:content:)-5jsgo)*