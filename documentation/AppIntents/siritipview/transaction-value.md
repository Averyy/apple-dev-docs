# transaction(value:_:)

**Framework**: App Intents  
**Kind**: method

Applies the given transaction mutation function to all animations used within the view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func transaction(value: some Equatable, _ transform: @escaping (inout Transaction) -> Void) -> some View
```

#### Return Value

A view that wraps this view and applies a transformation to all transactions used within the view whenever `value` changes.

#### Discussion

Use this modifier to change or replace the animation used in a view. Consider three identical views controlled by a button that changes all three simultaneously:

- The first view animates rotating the “Rotation” `Text` view by 360 degrees.
- The second uses the `transaction(_:)` modifier to change the animation by adding a delay to the start of the animation by two seconds and then increases the rotational speed of the “Rotation\nModified” `Text` view animation by a factor of 2.
- The third uses the `transaction(_:)` modifier to disable animations affecting the “Animation\nReplaced” `Text` view.

The following code implements these animations:

```swift
struct TransactionExample: View {
    @State var flag = false

    var body: some View {
        VStack(spacing: 50) {
            HStack(spacing: 30) {
                Text("Rotation")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))

                Text("Rotation\nModified")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))
                    .transaction(value: flag) { t in
                        t.animation =
                            t.animation?.delay(2.0).speed(2)
                    }

                Text("Animation\nReplaced")
                    .rotationEffect(Angle(degrees: flag ? 360 : 0))
                    .transaction(value: flag) { t in
                        t.disableAnimations = true
                    }
            }

            Button("Animate") {
                withAnimation(.easeIn(duration: 2.0)) {
                    flag.toggle()
                }
            }
        }
    }
}
```

## Parameters

- `value`: A value to monitor for changes.
- `transform`: The transformation to apply to transactions   within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/transaction(value:_:))*