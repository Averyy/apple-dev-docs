# NSUserInterfaceLayoutOrientation.horizontal

**Framework**: AppKit  
**Kind**: case

The horizontal orientation.

**Availability**:
- macOS 10.9+

## Declaration

```swift
case horizontal
```

#### Discussion

Use this constant in the [`orientation`](nsstackview/orientation.md) property to specify a horizontal layout for the stack view. Use it to specify the horizontal user interface axis for clipping resistance and hugging priority.

The leading, center, and trailing gravity areas in a horizontal stack view are arranged left to right or right to left depending on the value of the inherited [`userInterfaceLayoutDirection`](nsview/userinterfacelayoutdirection.md) property.

## See Also

- [NSUserInterfaceLayoutOrientation.vertical](nsuserinterfacelayoutorientation/vertical.md)
  The vertical orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacelayoutorientation/horizontal)*