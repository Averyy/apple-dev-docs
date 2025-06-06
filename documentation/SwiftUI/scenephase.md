# ScenePhase

**Framework**: SwiftUI  
**Kind**: enum

An indication of a scene’s operational state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum ScenePhase
```

## Mentions

- [Migrating to the SwiftUI life cycle](migrating-to-the-swiftui-life-cycle.md)

#### Overview

The system moves your app’s [`Scene`](scene.md) instances through phases that reflect a scene’s operational state. You can trigger actions when the phase changes. Read the current phase by observing the [`scenePhase`](environmentvalues/scenephase.md) value in the [`Environment`](environment.md):

```swift
@Environment(\.scenePhase) private var scenePhase
```

How you interpret the value depends on where it’s read from. If you read the phase from inside a [`View`](view.md) instance, you obtain a value that reflects the phase of the scene that contains the view. The following example uses the [`onChange(of:initial:_:)`](view/onchange(of:initial:_:)-8wgw9.md) method to enable a timer whenever the enclosing scene enters the [`ScenePhase.active`](scenephase/active.md) phase and disable the timer when entering any other phase:

```swift
struct MyView: View {
    @ObservedObject var model: DataModel
    @Environment(\.scenePhase) private var scenePhase

    var body: some View {
        TimerView()
            .onChange(of: scenePhase) {
                model.isTimerRunning = (scenePhase == .active)
            }
    }
}
```

If you read the phase from within an [`App`](app.md) instance, you obtain an aggregate value that reflects the phases of all the scenes in your app. The app reports a value of [`ScenePhase.active`](scenephase/active.md) if any scene is active, or a value of [`ScenePhase.inactive`](scenephase/inactive.md) when no scenes are active. This includes multiple scene instances created from a single scene declaration; for example, from a [`WindowGroup`](windowgroup.md). When an app enters the [`ScenePhase.background`](scenephase/background.md) phase, expect the app to terminate soon after. You can use that opportunity to free any resources:

```swift
@main
struct MyApp: App {
    @Environment(\.scenePhase) private var scenePhase

    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
        .onChange(of: scenePhase) {
            if scenePhase == .background {
                // Perform cleanup when all scenes within
                // MyApp go to the background.
            }
        }
    }
}
```

## Topics

### Getting scene phases
- [ScenePhase.active](scenephase/active.md)
  The scene is in the foreground and interactive.
- [ScenePhase.inactive](scenephase/inactive.md)
  The scene is in the foreground but should pause its work.
- [ScenePhase.background](scenephase/background.md)
  The scene isn’t currently visible in the UI.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var scenePhase: ScenePhase](environmentvalues/scenephase.md)
  The current phase of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenephase)*