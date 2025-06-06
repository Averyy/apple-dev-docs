# DismissImmersiveSpaceAction

**Framework**: SwiftUI  
**Kind**: struct

An action that dismisses an immersive space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
struct DismissImmersiveSpaceAction
```

#### Overview

Use the [`dismissImmersiveSpace`](environmentvalues/dismissimmersivespace.md) environment value to get an instance of this type for a given [`Environment`](environment.md). Then call the instance to dismiss a space. You call the instance directly because it defines a [`callAsFunction()`](dismissimmersivespaceaction/callasfunction().md) method that Swift calls when you call the instance.

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

## Topics

### Calling the action
- [func callAsFunction() async](dismissimmersivespaceaction/callasfunction.md)
  Dismisses the currently opened immersive space.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var dismissImmersiveSpace: DismissImmersiveSpaceAction](environmentvalues/dismissimmersivespace.md)
  An immersive space dismissal action stored in a view’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dismissimmersivespaceaction)*