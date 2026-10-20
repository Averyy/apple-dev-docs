# init(selection:in:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that selects multiple dates on or after some start date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(selection: Binding<Set<DateComponents>>, in bounds: PartialRangeUpTo<Date>, @ContentBuilder label: () -> Label)
```

```swift
nonisolated
init(selection: Binding<Set<DateComponents>>, in bounds: Range<Date>, @ContentBuilder label: () -> Label)
```

## Parameters

- `selection`: The date values being displayed and selected.
- `bounds`: The open range from some selectable start date.
- `label`: A view that describes the use of the dates.

## See Also

### Picking dates in a range
- [init(_:selection:in:)](./init%28_,selection,in%29.md)
  Creates an instance that selects multiple dates on or after some start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(selection:in:label:))*