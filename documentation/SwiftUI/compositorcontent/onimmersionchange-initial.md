# onImmersionChange(initial:_:)

**Framework**: SwiftUI  
**Kind**: method

Performs an action when the immersion state of your app changes.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func onImmersionChange(initial: Bool = true, _ action: @escaping (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some CompositorContent
```

#### Discussion

Depending on the immersion style used for the Immersive Space in your app, the amount of immersion can be controlled by actions such as turning the Digital Crown. Use this modifier to define a closure that is run when the immersion state changes.

## Parameters

- `initial`: Whether the action should be run when this view initially   appears.
- `action`: A closure to run when the immersion changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent/onimmersionchange(initial:_:))*