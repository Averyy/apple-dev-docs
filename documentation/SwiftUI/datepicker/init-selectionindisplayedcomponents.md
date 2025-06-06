# init(_:selection:in:displayedComponents:)

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
init(_ titleKey: LocalizedStringKey, selection: Binding<Date>, in range: ClosedRange<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date])
```

## Parameters

- `titleKey`: The key for the localized title of  , describing   its purpose.
- `selection`: The date value being displayed and selected.
- `range`: The inclusive range of selectable dates.
- `displayedComponents`: The date components that user is able to   view and edit. Defaults to  . On watchOS,   if   or   are included with   , only   is displayed.

## See Also

- [init(selection:in:displayedComponents:label:)](datepicker/init(selection:in:displayedcomponents:label:).md)
  Creates an instance that selects a `Date` in a closed range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepicker/init(_:selection:in:displayedcomponents:))*