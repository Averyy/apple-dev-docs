# accessibilityAction(named:_:)

**Framework**: PermissionKit  
**Kind**: method

Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityAction<S>(named name: S, _ handler: @escaping () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

#### Discussion

For example, this is how a custom action to compose a new email could be added to a view.

```None
var body: some View {
    ContentView()
        .accessibilityAction(named: "New Message") {
            // Handle action
        }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/accessibilityaction(named:_:)-7xv9g)*