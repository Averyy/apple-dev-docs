# gesturesForFailureRequirements

**Framework**: AppKit  
**Kind**: property

The gesture recognizers managed by the selection manager.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var gesturesForFailureRequirements: [NSGestureRecognizer] { get }
```

#### Discussion

Other gesture recognizers in the view hierarchy can declare dependencies on these gestures using `requireGestureRecognizerToFail:` to ensure proper gesture recognition precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/gesturesforfailurerequirements)*