# NSTableViewRowAction.Style.destructive

**Framework**: AppKit  
**Kind**: case

Apply a style that indicates that the action might change or delete data. This style changes the value of the [`backgroundColor`](nstableviewrowaction/backgroundcolor.md) property to an appropriate value to reflect the destructive action. After creating the action object, you can change the background color as needed. Destructive actions require a longer swipe to activate, and trigger an animation when a table row is deleted.

**Availability**:
- macOS 10.11+

## Declaration

```swift
case destructive
```

## See Also

- [NSTableViewRowAction.Style.regular](nstableviewrowaction/style-swift.enum/regular.md)
  Apply the default style to the button. This style does not apply any special coloring to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewrowaction/style-swift.enum/destructive)*