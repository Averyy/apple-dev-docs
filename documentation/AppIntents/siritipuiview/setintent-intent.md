# setIntent(intent:)

**Framework**: App Intents  
**Kind**: method

Sets an `AppIntent` for this view. This must be called before presenting the view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency final func setIntent<Intent>(intent: Intent) where Intent : AppIntent
```

#### Discussion

The provided `AppIntent` must be a valid App Shortcut for this view to work correctly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipuiview/setintent(intent:))*