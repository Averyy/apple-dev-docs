# init(selection:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that selects multiple dates with an unbounded range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(selection: Binding<Set<DateComponents>>, @ViewBuilder label: () -> Label)
```

## Parameters

- `selection`: The date values being displayed and selected.
- `label`: A view that describes the use of the dates.

## See Also

- [init(_:selection:)](multidatepicker/init(_:selection:).md)
  Creates an instance that selects multiple dates with an unbounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(selection:label:))*