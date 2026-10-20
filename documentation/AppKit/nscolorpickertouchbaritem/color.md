# color

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The picker’s currently selected color.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

*Mac Catalyst*

```swift
@NSCopying
var color: UIColor { get set }
```

*macOS*

```swift
@NSCopying
var color: NSColor { get set }
```

*Mac Catalyst*

```objc
@property (copy) UIColor * color;
```

*macOS*

```objc
@property (copy) NSColor * color;
```

## See Also

### Obtaining the selected color
- [var target: AnyObject?](./target.md)
  An object that is notified when a user interacts with the color picker.
- [var action: Selector?](./action.md)
  The selector on the target object that is invoked when a user interacts with the color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem/color)*