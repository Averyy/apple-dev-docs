# init(selection:label:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a picker that displays a custom label.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init(selection: Binding<SelectionValue>, label: Label, @ViewBuilder content: () -> Content)
```

## Parameters

- `selection`: A binding to a property that determines the currently-selected option.
- `label`: A view that describes the purpose of selecting an option.
- `content`: A view that contains the set of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/picker/init(selection:label:content:))*