# thickness

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The thickness of the status bar, in pixels.

**Availability**:
- macOS

## Declaration

```swift
var thickness: CGFloat { get }
```

```objc
@property (readonly) CGFloat thickness;
```

## Discussion

The default value of this property is `20.0`. The status bar returned by the [`system`](./system.md) has a thickness of 22 pixels, which corresponds to the thickness of the menu bar.

## See Also

### Getting Status-Bar Attributes
- [var isVertical: Bool](./isvertical.md)
  A Boolean value indicating whether the status bar has a vertical orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusbar/thickness)*