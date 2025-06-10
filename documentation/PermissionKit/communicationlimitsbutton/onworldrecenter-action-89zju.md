# onWorldRecenter(action:)

**Framework**: PermissionKit  
**Kind**: method

Adds an action to perform when recentering the view with the digital crown.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func onWorldRecenter(action: @escaping @MainActor (WorldRecenterPhase) -> Void) -> some View
```

#### Discussion

```None
struct ContentView: View {
    @State private var mascot = Mascot()
    var body: some View {
        WelcomeView(mascot: mascot)
            .onWorldRecenter { phase in
                switch phase {
                case .began:
                    prepareForReposition()
                case .ended:
                    mascot.wave()
                @unknown default:
                    break
                }
            }
    }
}
```

When the user recenters their view, first it will fade out, and the action will be called with a ‘began’ phase. After the app is repositioned, the action will be called again with an ‘ended’ phase and the app will fade back in. These actions will be called if the app is not backgrounded or suspended.

## Parameters

- `action`: A closure to run when the view is recentered. The closure   takes a   parameter that indicates the phase of the   recentering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/onworldrecenter(action:)-89zju)*