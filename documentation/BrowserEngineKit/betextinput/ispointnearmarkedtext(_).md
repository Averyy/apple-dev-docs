# isPointNearMarkedText(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides a Boolean value that indicates if a point is near marked text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func isPointNearMarkedText(_ point: CGPoint) -> Bool
```

```objc
- (BOOL) isPointNearMarkedText:(CGPoint) point;
```

## Discussion

The system uses the value you return to determine whether to begin text interaction gestures that occur close to the marked text.

## See Also

### Managing marked text
- [var hasMarkedText: Bool](./hasmarkedtext.md)
  A Boolean value that indicates if marked text exists for an active input session.
- [var markedTextRange: UITextRange?](./markedtextrange.md)
  A range that represents the position of the marked text.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/ispointnearmarkedtext(_:))*