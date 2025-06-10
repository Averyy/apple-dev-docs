# selectionDisabled(_:)

**Framework**: PermissionKit  
**Kind**: method

Adds a condition that controls whether users can select this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+ (Beta)
- watchOS 10.0+

## Declaration

```swift
nonisolated
func selectionDisabled(_ isDisabled: Bool = true) -> some View
```

#### Discussion

Use this modifier to control the selectability of views in selectable containers like `List` or `Table`. In the example, below, the user can’t select the first item in the list.

```None
@Binding var selection: Item.ID?
@Binding var items: [Item]

var body: some View {
    List(selection: $selection) {
        ForEach(items) { item in
            ItemView(item: item)
                .selectionDisabled(item.id == items.first?.id)
        }
    }
}
```

You can also use this modifier to specify the selectability of views within a `Picker`. The following example represents a flavor picker that disables selection on flavors that are unavailable.

```None
Picker("Flavor", selection: $selectedFlavor) {
    ForEach(Flavor.allCases) { flavor in
        Text(flavor.rawValue.capitalized)
            .selectionDisabled(isSoldOut(flavor))
    }
}
```

## Parameters

- `isDisabled`: A Boolean value that determines whether users can   select this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/selectiondisabled(_:))*