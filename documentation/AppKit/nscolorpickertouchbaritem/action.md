# action

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The selector on the target object that is invoked when a user interacts with the color picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var action: Selector? { get set }
```

```objc
@property (nullable) SEL action;
```

## See Also

### Obtaining the selected color
- [var color: UIColor](./color.md)
  The picker’s currently selected color.
- [var target: AnyObject?](./target.md)
  An object that is notified when a user interacts with the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/action)*