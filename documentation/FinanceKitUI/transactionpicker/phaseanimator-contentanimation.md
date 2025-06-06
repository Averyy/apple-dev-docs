# phaseAnimator(_:content:animation:)

**Framework**: FinanceKitUI  
**Kind**: method

Animates effects that you apply to a view over a sequence of phases that change continuously.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func phaseAnimator<Phase>(_ phases: some Sequence, @ViewBuilder content: @escaping (PlaceholderContentView<Self>, Phase) -> some View, animation: @escaping (Phase) -> Animation? = { _ in .default }) -> some View where Phase : Equatable
```

#### Discussion

When the modified view first appears, this modifier renders its `content` closure using the first phase as input to the closure, along with a proxy for the modified view. Apply effects to the proxy — and thus to the modified view — in a way that’s appropriate for the first phase value.

Right away, the modifier provides its `content` closure with the value of the second phase. Update the effects that you apply to the proxy view accordingly, and the modifier animates the change for you. As soon as the animation completes, the procedure repeats using successive phases until reaching the last phase, at which point the modifier loops back to the first phase.

## Parameters

- `phases`: The sequence of phases to cycle through. Ensure that the   sequence isn’t empty. If it is, SwiftUI logs a runtime warning and   also returns a visual warning as the output view.
- `content`: A view builder closure that takes two parameters: a proxy   value representing the modified view and the current phase.   You can apply effects to the proxy based on the current phase.
- `animation`: A closure that takes the current phase as input. Return   the animation to use when transitioning to the next phase. If you   return  , the transition doesn’t animate. If you don’t set this   parameter, SwiftUI uses a default animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/phaseanimator(_:content:animation:))*