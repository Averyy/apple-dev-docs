# updateSelection(extent:boundary:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Includes the text up to the given point in the current text selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func updateSelection(extent point: CGPoint, boundary granularity: UITextGranularity, completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
func updateSelection(extent point: CGPoint, boundary granularity: UITextGranularity) async -> Bool
```

```objc
- (void) updateSelectionWithExtentPoint:(CGPoint) point boundary:(UITextGranularity) granularity completionHandler:(void (^)(BOOL selectionEndIsMoving)) completionHandler;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

## Parameters

- `point`: The location in the document to include in the updated selection.
- `granularity`: The amount of text to include in the updated selection.
- `completionHandler`: A block you call after your text view handles the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/updateselection(extent:boundary:completionhandler:))*