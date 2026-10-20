# minimumWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum width of the menu in screen coordinates.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var minimumWidth: CGFloat { get set }
```

```objc
@property CGFloat minimumWidth;
```

#### Discussion

This property contains a value of type `CGFloat`, indicating the minimum width of the menu in screen coordinates.

The menu will not draw smaller than its minimum width, but may draw larger if it needs more space. The default value for this property is `0`.

## See Also

### Configuring Menu Size
- [var size: NSSize](./size.md)
  The size of the menu in screen coordinates


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/minimumwidth)*