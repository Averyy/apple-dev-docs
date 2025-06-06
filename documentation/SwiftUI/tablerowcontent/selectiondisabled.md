# selectionDisabled(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds a condition that controls whether users can select this row.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func selectionDisabled(_ isDisabled: Bool = true) -> some TableRowContent<Self.TableRowValue>
```

#### Discussion

Use this modifier to control the selectability of views in selectable containers like [`List`](list.md) or [`Table`](table.md). In the example, below, the user can’t select the first item in the table.

```swift
@Binding var rows: [Item]
@Binding var selection: Set<Item.ID>

var body: some View {
    Table(of: Item.self, selection: $selection) {
        TableColumn("ID", value: \.id.uuidString)
    } rows: {
        ForEach(rows) { row in
            TableRow(row)
                .selectionDisabled(
                    row.id == rows.first?.id
                )
        }
    }
}
```

You can also use this modifier to specify the selectability of views within a `Picker`. The following example represents a flavor picker that disables selection on flavors that are unavailable.

```swift
Picker("Flavor", selection: $selectedFlavor) {
    ForEach(Flavor.allCases) { flavor in
        Text(flavor.rawValue.capitalized)
            .selectionDisabled(isSoldOut(flavor))
    }
}
```

## Parameters

- `isDisabled`: A Boolean value that determines whether users   can select this row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowcontent/selectiondisabled(_:))*