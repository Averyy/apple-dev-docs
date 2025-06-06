# init(_:selection:displayedComponents:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that selects a `Date` with an unbounded range.

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
init(_ titleKey: LocalizedStringKey, selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date])
```

## Parameters

- `titleKey`: The key for the localized title of  , describing   its purpose.
- `selection`: The date value being displayed and selected.
- `displayedComponents`: The date components that user is able to   view and edit. Defaults to  . On watchOS,   if   or   are included with   , only   is displayed.

## See Also

- [init(selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components, label: () -> Label)](datepicker/init(selection:displayedcomponents:label:).md)
  Creates an instance that selects a `Date` with an unbounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepicker/init(_:selection:displayedcomponents:))*