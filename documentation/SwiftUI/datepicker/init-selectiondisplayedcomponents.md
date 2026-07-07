# init(_:selection:displayedComponents:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that selects a `Date` with an unbounded range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date])
```

## Parameters

- `titleResource`: The localized title of `self`, describing its purpose.
- `selection`: The date value being displayed and selected.
- `displayedComponents`: The date components that user is able to view and edit. Defaults to `[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or `.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

- [init(selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components, label: () -> Label)](datepicker/init(selection:displayedcomponents:label:).md)
  Creates an instance that selects a `Date` with an unbounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepicker/init(_:selection:displayedcomponents:))*