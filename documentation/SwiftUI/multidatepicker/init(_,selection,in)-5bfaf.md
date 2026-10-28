# init(_:selection:in:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that selects multiple dates in a range.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Set<DateComponents>>, in bounds: Range<Date>)
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeUpTo<Date>)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeUpTo<Date>)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<Set<DateComponents>>, in bounds: Range<Date>)
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeUpTo<Date>) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, selection: Binding<Set<DateComponents>>, in bounds: Range<Date>) where S : StringProtocol
```

## Parameters

- `titleResource`: The localized title of `self`, describing its purpose.
- `selection`: The date values being displayed and selected.
- `bounds`: The exclusive range of selectable dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(_:selection:in:)-5bfaf)*