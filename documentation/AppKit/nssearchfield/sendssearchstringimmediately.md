# sendsSearchStringImmediately

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell calls its action method immediately when an appropriate action occurs.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var sendsSearchStringImmediately: Bool { get set }
```

#### Discussion

When the value of this property is YES, the field calls its action method immediately upon notification of any changes to the search field. When the value is NO, the field pauses briefly after receiving a notification and then calls its action method. Pausing gives the user an opportunity to type more text into the search field and minimize the number of searches that are performed.

## See Also

- [var sendsWholeSearchString: Bool](nssearchfield/sendswholesearchstring.md)
  A Boolean value indicating whether the cell calls its search action method when the user clicks the search button or presses Return, or after each keystroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfield/sendssearchstringimmediately)*