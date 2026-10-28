# listSectionSpacing(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the spacing between adjacent sections in a [`List`](../list.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func listSectionSpacing(_ spacing: ListSectionSpacing) -> some View
```

**Other overloads**:

```swift
nonisolated
func listSectionSpacing(_ spacing: CGFloat) -> some View
```

## Discussion

Pass `.default` for the default spacing, or use `.compact` for a compact appearance between sections.

The following example creates a [`List`](../list.md) with compact spacing between sections:

```swift
List {
    Section("Colors") {
        Text("Blue")
        Text("Red")
    }

    Section("Shapes") {
        Text("Square")
        Text("Circle")
    }
}
.listSectionSpacing(.compact)
```

Spacing can also be specified on an individual [`Section`](../section.md), as in this example:

```swift
Section("Borders") {
    Text("Dashed")
    Text("Solid")
}
.listSectionSpacing(.compact)
```

Spacing applied on sections in the [`List`](../list.md) overrides spacing applied on the [`List`](../list.md) as a whole.

## Parameters

- `spacing`: The [`ListSectionSpacing`](../listsectionspacing.md) to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listsectionspacing(_:)-5t518)*