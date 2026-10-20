# shortcutsLinkStyle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the given style for ShortcutsLinks within the view hierarchy

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
nonisolated
func shortcutsLinkStyle(_ style: ShortcutsLinkStyle) -> some View
```

#### Return Value

A view that uses the specified shortcuts button style on its child views.

## Parameters

- `style`: The style to set.

## See Also

### App intents
- [func appEntityIdentifier(EntityIdentifier?) -> some View](./appentityidentifier%28_%29.md)
  Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [func appEntityIdentifier<I>(forSelectionType: I.Type, identifier: (I) -> EntityIdentifier?) -> some View](./appentityidentifier%28forselectiontype,identifier%29.md)
  Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [func appEntityUIElements((AppEntityUIElementsContext) -> [AppEntityUIElement]) -> some View](./appentityuielements%28_%29.md)
  Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [func onAppIntentExecution<I>(I.Type, perform: (I) -> Void) -> some View](./onappintentexecution%28_,perform%29.md)
  Registers a handler to run when the app receives an app intent that targets the associated scene.
- [func siriTipViewStyle(SiriTipViewStyle) -> some View](./siritipviewstyle%28_%29.md)
  Sets the given style for SiriTipView within the view hierarchy


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/shortcutslinkstyle(_:))*