# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the button is in an enabled state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

#### Discussion

When [`false`](../../Swift/false.md), CarPlay doesn’t call the button’s handler, and it changes the button’s appearance to reflect its disabled state.

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring the Button’s Attributes
- [var title: String?](./title.md)
  The button’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbutton/isenabled)*