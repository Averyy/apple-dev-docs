# onWorldRecenter(action:)

**Framework**: App Intents  
**Kind**: method

Adds an action to perform when recentering the view with the digital crown.

**Availability**:
- visionOS 26.0+ (Beta)

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

- `action`: A closure to run when the view is recentered. This will run   when the app has been recentered and is about to fade back in,   equivalent to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/onworldrecenter(action:)-3kpw8)*