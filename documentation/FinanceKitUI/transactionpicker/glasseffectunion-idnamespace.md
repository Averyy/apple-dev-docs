# glassEffectUnion(id:namespace:)

**Framework**: FinanceKitUI  
**Kind**: method

Associates any glass effects defined within this view to a union with the provided id.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View
```

#### Discussion

You may want the geometries of multiple views to contribute to a single glass effect shape. In these cases, you can use a `View/glassEffectUnion(id:namespace:)` to specify that a view should contribute to a union of glass effects with a particular id. All glass effects with the same shape and glass will be combined into a single shape.

In the example below, two shapes are rendered on the leading and trailing edge each encapsulating two distinct views.

```None
enum PlacementGroup: Hashable {
    case leading
    case trailing
    case spacer
}

struct Item: Identifiable {
    var id: String
    var placement: Placement
}

@State private var items: [Item] = [
    Item(id: "0", placement: .leading),
    Item(id: "1", placement: .leading),
    Item(id: "spacer", placement: .spacer),
    Item(id: "2", placement: .trailing),
    Item(id: "3", placement: .trailing)
]
@Namespace private var namespace

var body: some View {
    GlassEffectContainer {
        HStack {
            ForEach(items) { item in
                itemView(item)
            }
        }
    }
}

func itemView(_ item: Item) -> some View {
    VStack {
        if item.placement == .spacer {
            Spacer()
        } else {
            Text(items.id)
                .padding()
                .glassEffect()
                .glassEffectUnion(id: item.placement, namespace: namespace)
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/glasseffectunion(id:namespace:))*