# supportsRemoteScenes

**Framework**: SwiftUI  
**Kind**: property

Indicates if the current device supports presenting a [`RemoteImmersiveSpace`](remoteimmersivespace.md) on a remote device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var supportsRemoteScenes: Bool { get }
```

#### Discussion

Use this to provide affordances for displaying your app’s content on a remote device.

```swift
struct NewSolarSystemImmersiveSpaceButton: View {
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace
    @Environment(\.supportsRemoteScenes) private var supportsRemoteScenes

    var body: some View {
        Button("Present Solar System") {
            Task {
                await openImmersiveSpace(id: "solarSystem")
            }
        }
        .disabled(!supportsRemoteScenes)
        .help(!supportsRemoteScenes
            ? "Presenting remote scenes is not supported on this device."
            : "")
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/supportsremotescenes)*