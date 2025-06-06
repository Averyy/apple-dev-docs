# accessibilityHidden(_:isEnabled:)

**Framework**: App Intents  
**Kind**: method

Specifies whether to hide this view from system accessibility features.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityHidden(_ hidden: Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `hidden`: Whether to hide this view from accessibility features.
- `isEnabled`: If true the accessibility hidden state is applied;   otherwise the accessibility hidden state is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/accessibilityhidden(_:isenabled:))*