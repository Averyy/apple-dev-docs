# hasMarkedText

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates if marked text exists for an active input session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var hasMarkedText: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasMarkedText;
```

## See Also

### Managing marked text
- [var markedTextRange: UITextRange?](./markedtextrange.md)
  A range that represents the position of the marked text.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.
- [func isPointNearMarkedText(CGPoint) -> Bool](./ispointnearmarkedtext%28_%29.md)
  Provides a Boolean value that indicates if a point is near marked text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/hasmarkedtext)*