# init(_:selection:)

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
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Set<DateComponents>>)
```

## Parameters

- `titleResource`: The localized title of `self`, describing its purpose.
- `selection`: The date values being displayed and selected.

## See Also

- [init(selection: Binding<Set<DateComponents>>, label: () -> Label)](multidatepicker/init(selection:label:).md)
  Creates an instance that selects multiple dates with an unbounded range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/multidatepicker/init(_:selection:))*