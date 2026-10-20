# cancelAutoscroll()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates that the current autoscroll gesture is complete.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func cancelAutoscroll()
```

```objc
- (void) cancelAutoscroll;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

When the text system calls this method on your text view, there are no more calls to [`autoscroll(to:)`](./autoscroll%28to%29.md) for the current text interaction gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/cancelautoscroll())*