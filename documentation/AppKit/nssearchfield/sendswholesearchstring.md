# sendsWholeSearchString

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell calls its search action method when the user clicks the search button or presses Return, or after each keystroke.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var sendsWholeSearchString: Bool { get set }
```

#### Discussion

When the value of this property is yes, the field calls its action method when the user clicks the search button or presses Return. When the value is NO, the field calls the action method after each keystroke. The default value of this property is no.

## See Also

- [var sendsSearchStringImmediately: Bool](nssearchfield/sendssearchstringimmediately.md)
  A Boolean value indicating whether the cell calls its action method immediately when an appropriate action occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/sendswholesearchstring)*