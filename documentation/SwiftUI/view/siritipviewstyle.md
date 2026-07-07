# siriTipViewStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the given style for SiriTipView within the view hierarchy

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func siriTipViewStyle(_ style: SiriTipViewStyle) -> some View
```

#### Return Value

A view that uses the specified style on its child views.

## Parameters

- `style`: The style to set.

## See Also

- [func appEntityIdentifier(EntityIdentifier?) -> some View](view/appentityidentifier(_:).md)
  Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [func appEntityIdentifier<I>(forSelectionType: I.Type, identifier: (I) -> EntityIdentifier?) -> some View](view/appentityidentifier(forselectiontype:identifier:).md)
  Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [func appEntityUIElements((AppEntityUIElementsContext) -> [AppEntityUIElement]) -> some View](view/appentityuielements(_:).md)
  Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [func onAppIntentExecution<I>(I.Type, perform: (I) -> Void) -> some View](view/onappintentexecution(_:perform:).md)
  Registers a handler to invoke in response to the specified app intent that your app receives.
- [func shortcutsLinkStyle(ShortcutsLinkStyle) -> some View](view/shortcutslinkstyle(_:).md)
  Sets the given style for ShortcutsLinks within the view hierarchy


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/siritipviewstyle(_:))*