# transaction(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies the given transaction mutation function to all animations used within the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transaction(_ transform: @escaping (inout Transaction) -> Void) -> some View
```

#### Return Value

A view that wraps this view and applies a transformation to all transactions used within the view.

#### Discussion

Use this modifier to change or replace the animation used in a view. Consider three identical animations controlled by a button that executes all three animations simultaneously:

- The first animation rotates the “Rotation” [`Text`](text.md) view by 360 degrees.
- The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” [`Text`](text.md) view animation by a factor of 2.
- The third animation uses the `transaction(_:)` modifier to replace the rotation animation affecting the “Animation\nReplaced” [`Text`](text.md) view with a spring animation.

The following code implements these animations:

```swift
struct TransactionExample: View {
    @State private var flag = false

    var body: some View {
        VStack(spacing: 50) {
            HStack(spacing: 30) {
                Text("Rotation")
                    .rotationEffect(Angle(degrees:
                                            self.flag ? 360 : 0))

                Text("Rotation\nModified")
                    .rotationEffect(Angle(degrees:
                                            self.flag ? 360 : 0))
                    .transaction { view in
                        view.animation =
                            view.animation?.delay(2.0).speed(2)
                    }

                Text("Animation\nReplaced")
                    .rotationEffect(Angle(degrees:
                                            self.flag ? 360 : 0))
                    .transaction { view in
                        view.animation = .interactiveSpring(
                            response: 0.60,
                            dampingFraction: 0.20,
                            blendDuration: 0.25)
                    }
            }

            Button("Animate") {
                withAnimation(.easeIn(duration: 2.0)) {
                    self.flag.toggle()
                }
            }
        }
    }
}
```

Use this modifier on leaf views such as [`Image`](image.md) or [`Button`](button.md) rather than container views such as [`VStack`](vstack.md) or [`HStack`](hstack.md). The transformation applies to all child views within this view; calling `transaction(_:)` on a container view can lead to unbounded scope of execution depending on the depth of the view hierarchy.

## Parameters

- `transform`: The transformation to apply to transactions   within this view.

## See Also

- [func withTransaction<Result>(Transaction, () throws -> Result) rethrows -> Result](withtransaction(_:_:).md)
  Executes a closure with the specified transaction and returns the result.
- [func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws -> R) rethrows -> R](withtransaction(_:_:_:).md)
  Executes a closure with the specified transaction key path and value and returns the result.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](view/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](view/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [struct Transaction](transaction.md)
  The context of the current state-processing update.
- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.
- [protocol TransactionKey](transactionkey.md)
  A key for accessing values in a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/transaction(_:))*