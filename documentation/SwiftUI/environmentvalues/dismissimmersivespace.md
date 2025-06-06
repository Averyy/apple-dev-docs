# dismissImmersiveSpace

**Framework**: SwiftUI  
**Kind**: property

An immersive space dismissal action stored in a view’s environment.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var dismissImmersiveSpace: DismissImmersiveSpaceAction { get }
```

#### Discussion

Use this environment value to get a [`DismissImmersiveSpaceAction`](dismissimmersivespaceaction.md) instance for a given [`Environment`](environment.md). Then call the instance to dismiss a space. You call the instance directly because it defines a [`callAsFunction()`](dismissimmersivespaceaction/callasfunction().md) method that Swift calls when you call the instance.

For example, you can define a button that dismisses an immersive space:

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            DismissImmersiveSpaceButton()
        }
        ImmersiveSpace(id: "solarSystem") {
            SolarSystemView()
        }
    }
}

struct DismissImmersiveSpaceButton: View {
    @Environment(\.dismissImmersiveSpace) private var dismissImmersiveSpace

    var body: some View {
        Button("Dismiss") {
            Task {
                await dismissImmersiveSpace()
            }
        }
    }
}
```

The asynchronous call returns after the system finishes dismissing the space. Unlike the call to [`openImmersiveSpace`](environmentvalues/openimmersivespace.md) that you use to open the space — which requires an identifier, a value, or both to specify which space to open — the dismiss action requires no parameters because there can be only one immersive space open at a time. The call closes the space that is currently open, if any.

## See Also

- [struct DismissImmersiveSpaceAction](dismissimmersivespaceaction.md)
  An action that dismisses an immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/dismissimmersivespace)*