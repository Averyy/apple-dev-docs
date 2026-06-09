# onWorldRecenter(action:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when recentering the view with the digital crown.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func onWorldRecenter(action: @escaping @MainActor () -> Void) -> some View
```

#### Discussion

```swift
struct ContentView: View {
    @State private var mascot = Mascot()
    var body: some View {
        WelcomeView(mascot: mascot)
            .onWorldRecenter {
                mascot.wave()
            }
    }
}
```

When the user recenters their view, the app will fade out and then be repositioned. Once it has been repositioned, the action will be called and the app will fade back in. The action will be called if the app is not backgrounded or suspended.

## Parameters

- `action`: A closure to run when the view is recentered. This will run when the app has been recentered and is about to fade back in, equivalent to `WorldRecenterPhase.ended`.

## See Also

- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](view/onimmersionchange(initial:_:).md)
  Performs an action when the immersion state of your app changes.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](view/immersiveenvironmentpicker(content:).md)
  Add menu items to open immersive spaces from a media player’s environment picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onworldrecenter(action:))*