# sendsSearchStringImmediately

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell calls its action method immediately when an appropriate action occurs.

**Availability**:
- macOS

## Declaration

```swift
var sendsSearchStringImmediately: Bool { get set }
```

```objc
@property BOOL sendsSearchStringImmediately;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell calls its action method immediately upon notification of any changes to the search field. When the value is [`false`](../../Swift/false.md), the cell pauses briefly after receiving a notification and then calls its action method. Pausing gives the user an opportunity to type more text into the search field and minimize the number of searches that are performed.

## See Also

### Managing search modes
- [var sendsWholeSearchString: Bool](./sendswholesearchstring.md)
  A Boolean value indicating whether the cell calls its search action method when the user clicks the search button (or presses Return) or after each keystroke.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/sendssearchstringimmediately)*