# onImmersionChange(initial:_:)

**Framework**: SwiftUI  
**Kind**: method

Performs an action when the immersion state of your app changes.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func onImmersionChange(initial: Bool = true, _ action: @escaping (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View
```

#### Discussion

Depending on the immersion style used for the Immersive Space in your app, the amount of immersion can be controlled by actions such as turning the Digital Crown. Use this modifier to define a closure that is run when the immersion state changes. The following example sets the value of a binding depending on the current amount of immersion:

```swift
struct ImmersiveView: View {
    @Binding var enableSoundEffects: Bool

    var body: some View {
        MyView()
            .onImmersionChange { _, newImmersion in
                guard let amount = newImmersion.amount else {
                    enableSoundEffects = false
                    return
                }
                // Enable some effects based on the updated
                // amount of immersion
                enableSoundEffects = amount > 0.5
            }
    }
}
```

## Parameters

- `initial`: Whether the action should be run when this view initially   appears.
- `action`: A closure to run when the immersion changes.

## See Also

- [struct ImmersionChangeContext](immersionchangecontext.md)
  A structure that represents a state of immersion of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onimmersionchange(initial:_:))*