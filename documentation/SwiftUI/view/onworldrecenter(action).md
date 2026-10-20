# onWorldRecenter(action:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when recentering the view with the digital crown.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func onWorldRecenter(action: @escaping @MainActor () -> Void) -> some View
```

**Other overloads**:

```swift
nonisolated
func onWorldRecenter(action: @escaping @MainActor (WorldRecenterPhase) -> Void) -> some View
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

### Immersive spaces
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](./onimmersionchange%28initial,_%29.md)
  Performs an action when the immersion state of your app changes.
- [func immersiveEnvironmentPicker<Content>(content: () -> Content) -> some View](./immersiveenvironmentpicker%28content%29.md)
  Add menu items to open immersive spaces from a media player’s environment picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onworldrecenter(action:))*