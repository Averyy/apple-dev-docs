# headerProminence(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the header prominence for this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func headerProminence(_ prominence: Prominence) -> some View
```

#### Discussion

In the following example, the section header appears with increased prominence:

```swift
List {
    Section(header: Text("Header")) {
        Text("Row")
    }
    .headerProminence(.increased)
}
.listStyle(.insetGrouped)
```

## Parameters

- `prominence`: The prominence to apply.

## See Also

- [var headerProminence: Prominence](environmentvalues/headerprominence.md)
  The prominence to apply to section headers within a view.
- [enum Prominence](prominence.md)
  A type indicating the prominence of a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/headerprominence(_:))*