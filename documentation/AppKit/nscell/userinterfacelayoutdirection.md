# userInterfaceLayoutDirection

**Framework**: AppKit  
**Kind**: property

The layout direction of the user interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection { get set }
```

#### Discussion

This property specifies the general user interface layout flow directions. For subclasses that have multiple visual components in a single cell instance, this property should specify the directionality or flow of components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/userinterfacelayoutdirection)*