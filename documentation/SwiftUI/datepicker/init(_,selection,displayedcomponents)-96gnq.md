# init(_:selection:displayedComponents:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date])
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date]) where S : StringProtocol
```

## Parameters

- `titleKey`: The key for the localized title of `self`, describing its purpose.
- `selection`: The date value being displayed and selected.
- `displayedComponents`: The date components that user is able to view and edit. Defaults to `[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or `.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepicker/init(_:selection:displayedcomponents:)-96gnq)*