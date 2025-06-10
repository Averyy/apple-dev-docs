# isPresented

**Framework**: App Intents  
**Kind**: property

Determines if the view should be presented to the user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc @preconcurrency dynamic final var isPresented: Bool { get set }
```

#### Discussion

Defaults to `true` and gets set to `false` after the dismissal button is tapped. Changing this has no affect if `allowsDismissal` is set to `false`. This value is KVO compliant.

## See Also

- [var allowsDismissal: Bool](siritipuiview/allowsdismissal.md)
  Indicates if the tip view should display a dismissal button


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipuiview/ispresented)*