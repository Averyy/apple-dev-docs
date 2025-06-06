# scrollTargetAnchor

**Framework**: SwiftUI  
**Kind**: property

The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var scrollTargetAnchor: UnitPoint? { get set }
```

#### Discussion

Use this API in conjunction with a `ScrollViewProxy/scrollTo(_:anchor)` or when updating the binding provided to a [`scrollPosition(id:anchor:)`](view/scrollposition(id:anchor:).md).

```swift
@Binding var position: Item.ID?

var body: some View {
    ScrollView {
        LazyVStack {
            ForEach(items) { item in
                ItemView(item)
            }
        }
        .scrollTargetLayout()
    }
    .scrollPosition(id: $position)
    .safeAreaInset(edge: .bottom) {
        Button("Scroll To Bottom") {
            withAnimation {
                withTransaction(\.scrollTargetAnchor, .bottom) {
                    position = items.last?.id
                }
            }
        }
    }
}
```

When used with the [`scrollPosition(id:anchor:)`](view/scrollposition(id:anchor:).md) modifier, this value will be preferred over the anchor specified in the modifier for the current transaction.

## See Also

- [var isContinuous: Bool](transaction/iscontinuous.md)
  A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.
- [var tracksVelocity: Bool](transaction/tracksvelocity.md)
  Whether this transaction will track the velocity of any animatable properties that change.
- [subscript<K>(K.Type) -> K.Value](transaction/subscript(_:).md)
  Accesses the transaction value associated with a custom key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transaction/scrolltargetanchor)*