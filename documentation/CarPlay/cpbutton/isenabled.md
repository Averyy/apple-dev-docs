# isEnabled

**Framework**: CarPlay  
**Kind**: property

A Boolean value that determines whether the button is in an enabled state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

#### Discussion

When [`false`](https://developer.apple.com/documentation/swift/false), CarPlay doesn’t call the button’s handler, and it changes the button’s appearance to reflect its disabled state.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var title: String?](cpbutton/title.md)
  The button’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbutton/isenabled)*