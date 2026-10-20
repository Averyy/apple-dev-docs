# sendsWholeSearchString

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell calls its search action method when the user clicks the search button (or presses Return) or after each keystroke.

**Availability**:
- macOS

## Declaration

```swift
var sendsWholeSearchString: Bool { get set }
```

```objc
@property BOOL sendsWholeSearchString;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell calls its action method when the user clicks the search button or presses Return. When the value is [`false`](../../Swift/false.md), the cell calls the action method after each keystroke. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Managing search modes
- [var sendsSearchStringImmediately: Bool](./sendssearchstringimmediately.md)
  A Boolean value indicating whether the cell calls its action method immediately when an appropriate action occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchfieldcell/sendswholesearchstring)*