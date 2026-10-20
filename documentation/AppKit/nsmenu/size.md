# size

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the menu in screen coordinates

**Availability**:
- macOS 10.6+

## Declaration

```swift
var size: NSSize { get }
```

```objc
@property (readonly) NSSize size;
```

#### Discussion

This property contains a value of type `NSSize`, indicating the size of the menu in screen coordinates.

The menu may draw at a smaller size when shown, depending on its positioning and display configuration.

## See Also

### Configuring Menu Size
- [var minimumWidth: CGFloat](./minimumwidth.md)
  The minimum width of the menu in screen coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/size)*