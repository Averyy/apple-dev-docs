# init(selection:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that selects multiple dates with an unbounded range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(selection: Binding<Set<DateComponents>>, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View`.

## Parameters

- `selection`: The date values being displayed and selected.
- `label`: A view that describes the use of the dates.

## See Also

### Picking dates
- [init(_:selection:)](./init%28_,selection%29.md)
  Creates an instance that selects multiple dates with an unbounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(selection:label:))*