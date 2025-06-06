# target

**Framework**: AppKit  
**Kind**: property

An object that is notified when a user interacts with the color picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
weak var target: AnyObject? { get set }
```

## See Also

- [var color: UIColor](nscolorpickertouchbaritem/color.md)
  The picker’s currently selected color.
- [var action: Selector?](nscolorpickertouchbaritem/action.md)
  The selector on the target object that is invoked when a user interacts with the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/target)*