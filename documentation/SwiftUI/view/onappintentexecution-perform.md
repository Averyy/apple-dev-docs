# onAppIntentExecution(_:perform:)

**Framework**: SwiftUI  
**Kind**: method

Registers a handler to invoke in response to the specified app intent that your app receives.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func onAppIntentExecution<I>(_ intent: I.Type = I.self, perform action: @escaping @MainActor (I) -> Void) -> some View where I : TargetContentProvidingIntent
```

#### Return Value

A view that handles the specified app intent’s perform

#### Discussion

Use this view modifier to receive instances in a particular scene within your app. The scene that SwiftUI routes the incoming user activity to depends on the structure of your app, what scenes are active, and other configuration. For more information, see [`handlesExternalEvents(matching:)`](scene/handlesexternalevents(matching:).md).

The action closure is called before the app is foregrounded. If the app intent implements a perform() method, it will be called after the action closure. This can be useful if your app intent supports running in the background via the AppIntent.IntentModes API.

> **Note**: Usage of the app intent instance provided to the action closure is limited to inspecting parameter values, interactive requests like [`requestValue(_:)`](https://developer.apple.com/documentation/appintents/intentparameter/requestvalue(_:)-592nd) or [`needsValueError(_:)`](https://developer.apple.com/documentation/appintents/intentparameter/needsvalueerror(_:)) doesn’t work.

## Parameters

- `intent`: The type of App Intent that the `action` closure handles.
- `action`: A closure that SwiftUI calls when the specified app intent is being performed. The closure takes the app intent instance as an input parameter.

## See Also

- [func appEntityIdentifier(EntityIdentifier?) -> some View](view/appentityidentifier(_:).md)
  Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [func appEntityIdentifier<I>(forSelectionType: I.Type, identifier: (I) -> EntityIdentifier?) -> some View](view/appentityidentifier(forselectiontype:identifier:).md)
  Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [func appEntityUIElements((AppEntityUIElementsContext) -> [AppEntityUIElement]) -> some View](view/appentityuielements(_:).md)
  Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View](view/shortcutslinkstyle(_:).md)
  Sets the given style for ShortcutsLinks within the view hierarchy
- [func siriTipViewStyle(SiriTipViewStyle) -> some View](view/siritipviewstyle(_:).md)
  Sets the given style for SiriTipView within the view hierarchy


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onappintentexecution(_:perform:))*