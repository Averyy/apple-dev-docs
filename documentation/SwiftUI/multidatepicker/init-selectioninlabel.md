# init(selection:in:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that selects multiple dates on or after some start date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>, @ViewBuilder label: () -> Label)
```

## Parameters

- `selection`: The date values being displayed and selected.
- `bounds`: The open range from some selectable start date.
- `label`: A view that describes the use of the dates.

## See Also

- [init(_:selection:in:)](multidatepicker/init(_:selection:in:).md)
  Creates an instance that selects multiple dates on or after some start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(selection:in:label:))*