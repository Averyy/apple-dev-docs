# accessibilityAction(named:_:)

**Framework**: PermissionKit  
**Kind**: method

Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accessibilityAction(named nameResource: LocalizedStringResource, _ handler: @escaping () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
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

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/accessibilityaction(named:_:)-7nyf7)*