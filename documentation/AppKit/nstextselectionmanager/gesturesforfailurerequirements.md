# gesturesForFailureRequirements

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The gesture recognizers managed by the selection manager.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var gesturesForFailureRequirements: [NSGestureRecognizer] { get }
```

```objc
@property (readonly) NSArray<NSGestureRecognizer *> * gesturesForFailureRequirements;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## Discussion

Other gesture recognizers in the view hierarchy can declare dependencies on these gestures using `requireGestureRecognizerToFail:` to ensure proper gesture recognition precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/gesturesforfailurerequirements)*