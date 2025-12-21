# isVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating if the menu bar currently displays the status item.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var isVisible: Bool { get set }
```

#### Discussion

Setting this property either shows or hides the status item within the menu bar. The item’s visiblity may also change if the user removes the item manually, and you can watch for changes in visibility using key-value observation. The status item’s visiblity persists and restores automatically based on the value of [`autosaveName`](nsstatusitem/autosavename-swift.property.md).

This property returns [`true`](https://developer.apple.com/documentation/Swift/true) even if the status item is temporarily hidden due to insufficient space in the menu bar. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var length: CGFloat](nsstatusitem/length.md)
  The amount of space in the status bar that should be allocated to the status item.
- [class let squareLength: CGFloat](nsstatusitem/squarelength.md)
  A status item length that is equal to the status bar’s thickness.
- [class let variableLength: CGFloat](nsstatusitem/variablelength.md)
  A status item length that dynamically adjusts to the width of its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem/isvisible)*