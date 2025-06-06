# listSectionSpacing(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the spacing between adjacent sections in a `List`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func listSectionSpacing(_ spacing: ListSectionSpacing) -> some View
```

#### Discussion

Pass `.default` for the default spacing, or use `.compact` for a compact appearance between sections.

The following example creates a `List` with compact spacing between sections:

```None
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

Spacing can also be specified on an individual `Section`, as in this example:

```None
Section("Borders") {
    Text("Dashed")
    Text("Solid")
}
.listSectionSpacing(.compact)
```

Spacing applied on sections in the `List` overrides spacing applied on the `List` as a whole.

## Parameters

- `spacing`: The   to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/listsectionspacing(_:)-1wgnu)*