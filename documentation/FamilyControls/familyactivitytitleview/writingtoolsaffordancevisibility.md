# writingToolsAffordanceVisibility(_:)

**Framework**: FamilyControls  
**Kind**: method

Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
@MainActor
@preconcurrency func writingToolsAffordanceVisibility(_ visibility: Visibility) -> some View
```

#### Return Value

A view with the specified Writing Tools affordance visibility.

#### Discussion

Use this view modifier to disable the Writing Tools affordance for `TextField` views when running on macOS or Mac Catalyst.

## Parameters

- `visibility`: Whether the affordance may be shown for text   input views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/writingtoolsaffordancevisibility(_:))*