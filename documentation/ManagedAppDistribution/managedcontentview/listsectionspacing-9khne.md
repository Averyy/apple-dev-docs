# listSectionSpacing(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Sets the spacing between adjacent sections in a `List` to a custom value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func listSectionSpacing(_ spacing: CGFloat) -> some View
```

#### Discussion

The following example creates a `List` with 5 pts of spacing between sections:

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
.listSectionSpacing(5.0)
```

Spacing can also be specified on an individual `Section`, as in this example:

```None
Section("Borders") {
    Text("Dashed")
    Text("Solid")
}
.listSectionSpacing(10.0)
```

If adjacent sections have different spacing applied, each section applies half its spacing above and below. Sections without explicit spacing apply the spacing of their adjacent sections.

```None
List {
    Section("Colors") {
        Text("Blue")
        Text("Red")
    }

    Section("Borders") {
        Text("Dashed")
        Text("Solid")
    }
    .listSectionSpacing(10.0)

    Section("Shapes") {
        Text("Square")
        Text("Circle")
    }
    .listSectionSpacing(100.0)
}
```

In the above example, the “Colors” and “Borders” section are separated by 10 pts of spacing, and the “Borders” and “Shapes” section are separated by 55 pts of spacing.

Spacing applied on sections in the `List` overrides spacing applied on the `List` as a whole.

## Parameters

- `spacing`: The amount of spacing to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/listsectionspacing(_:)-9khne)*