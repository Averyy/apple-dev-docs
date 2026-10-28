# moveSelection(atBoundary:in:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Moves the text-selection caret relative to the current position.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func moveSelection(atBoundary granularity: UITextGranularity, in direction: UITextStorageDirection, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func moveSelection(atBoundary granularity: UITextGranularity, in direction: UITextStorageDirection) async
```

```objc
- (void) moveSelectionAtBoundary:(UITextGranularity) granularity inStorageDirection:(UITextStorageDirection) direction completionHandler:(void (^)()) completionHandler;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

## Discussion

If you return `false` from [`textInteractionGesture(_:shouldBeginAt:)`](./textinteractiongesture%28_,shouldbeginat%29.md) for the gesture that moves the caret, then the text system doesn’t call this method.

## Parameters

- `granularity`: The amount by which to move the caret.
- `direction`: The direction in which to move the caret, relative to the base writing direction.
- `completionHandler`: A block you call when your text view has handled the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/moveselection(atboundary:in:completionhandler:))*