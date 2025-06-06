# init(selection:in:displayedComponents:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that selects a `Date` in a closed range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(selection: Binding<Date>, in range: ClosedRange<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date], @ViewBuilder label: () -> Label)
```

## Parameters

- `selection`: The date value being displayed and selected.
- `range`: The inclusive range of selectable dates.
- `displayedComponents`: The date components that user is able to   view and edit. Defaults to  . On watchOS,   if   or   are included with   , only   is displayed.
- `label`: A view that describes the use of the date.

## See Also

- [init(_:selection:in:displayedComponents:)](datepicker/init(_:selection:in:displayedcomponents:).md)
  Creates an instance that selects a `Date` in a closed range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepicker/init(selection:in:displayedcomponents:label:))*