# init(selection:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a list with the given content that supports selecting a single row.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(selection: Binding<SelectionValue?>?, @ContentBuilder content: () -> Content)
```

**Other overloads**:

```swift
nonisolated
init(selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

```swift
nonisolated
init(selection: Binding<Set<SelectionValue>>?, @ContentBuilder content: () -> Content)
```

## Parameters

- `selection`: A binding to a selected row.
- `content`: The content of the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(selection:content:)-1pisz)*