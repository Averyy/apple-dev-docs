# accessibilityActions(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds multiple accessibility actions to the view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityActions<Content>(@ViewBuilder _ content: () -> Content) -> some View where Content : View
```

#### Discussion

Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. For example, this is how a dynamic number of custom action could be added to a view.

```swift
var isDraft: Bool

var body: some View {
    ContentView()
        .accessibilityActions {
            ForEach(actions) { action in
                Button {
                    action()
                } label: {
                    Text(action.title)
                }
            }

            if isDraft {
                Button {
                    // Handle Delete
                } label: {
                    Text("Delete")
                }
            }
        }
```

## See Also

- [func accessibilityAction(AccessibilityActionKind, () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityaction(_:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction(named:_:)](view/accessibilityaction(named:_:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<Label>(action: () -> Void, label: () -> Label) -> some View](view/accessibilityaction(action:label:).md)
  Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityAction<I, Label>(intent: I, label: () -> Label) -> some View](view/accessibilityaction(intent:label:).md)
  Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction<I>(AccessibilityActionKind, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityaction(_:intent:).md)
  Adds an accessibility action representing `actionKind` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAction(named:intent:)](view/accessibilityaction(named:intent:).md)
  Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.
- [func accessibilityAdjustableAction((AccessibilityAdjustmentDirection) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityadjustableaction(_:).md)
  Adds an accessibility adjustable action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityScrollAction((Edge) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityscrollaction(_:).md)
  Adds an accessibility scroll action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.
- [func accessibilityActions<Content>(category: AccessibilityActionCategory, () -> Content) -> some View](view/accessibilityactions(category:_:).md)
  Adds multiple accessibility actions to the view with a specific category. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action and are grouped by their category. When multiple action modifiers with an equal category are applied to the view, the actions are combined together.
- [struct AccessibilityActionKind](accessibilityactionkind.md)
  The structure that defines the kinds of available accessibility actions.
- [enum AccessibilityAdjustmentDirection](accessibilityadjustmentdirection.md)
  A directional indicator you use when making an accessibility adjustment.
- [struct AccessibilityActionCategory](accessibilityactioncategory.md)
  Designates an accessibility action category that is provided and named by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityactions(_:))*