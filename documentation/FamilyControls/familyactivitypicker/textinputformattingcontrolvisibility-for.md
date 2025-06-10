# textInputFormattingControlVisibility(_:for:)

**Framework**: FamilyControls  
**Kind**: method

Define which system text formatting controls are available.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func textInputFormattingControlVisibility(_ visibility: Visibility, for placement: TextInputFormattingControlPlacement.Set) -> some View
```

## Parameters

- `visibility`: Whether the control may become visible to the user
- `placement`: The onscreen control to modify


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/textinputformattingcontrolvisibility(_:for:))*