# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the text layout manager object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any NSTextLayoutManagerDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSTextLayoutManagerDelegate> delegate;
```

## See Also

### Managing the layout process
- [protocol NSTextLayoutManagerDelegate](../nstextlayoutmanagerdelegate.md)
  Optional methods that delegates implement to respond to layout changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/delegate)*