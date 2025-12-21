# sendsWholeSearchString

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell calls its search action method when the user clicks the search button (or presses Return) or after each keystroke.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var sendsWholeSearchString: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the cell calls its action method when the user clicks the search button or presses Return. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the cell calls the action method after each keystroke. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var sendsSearchStringImmediately: Bool](nssearchfieldcell/sendssearchstringimmediately.md)
  A Boolean value indicating whether the cell calls its action method immediately when an appropriate action occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/sendswholesearchstring)*