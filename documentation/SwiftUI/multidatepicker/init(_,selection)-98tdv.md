# init(_:selection:)

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
init<S>(_ title: S, selection: Binding<Set<DateComponents>>) where S : StringProtocol
```

Available when `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Set<DateComponents>>)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, selection: Binding<Set<DateComponents>>)
```

## Parameters

- `title`: The title of `self`, describing its purpose.
- `selection`: The date values being displayed and selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(_:selection:)-98tdv)*