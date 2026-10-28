# controlTint

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroller’s control tint.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Has had no effect since 10.7

## Declaration

```swift
var controlTint: NSControlTint { get set }
```

```objc
@property NSControlTint controlTint;
```

## Discussion

The valid values for `controlTint` are described in [`NSControlTint`](../nscontroltint.md).

> **Note**:  This method has no effect in macOS 10.7 and later.

## See Also

### Deprecated properties
- [var arrowsPosition: NSScroller.ArrowPosition](./arrowsposition.md)
  The location of the scroll buttons within the scroller, as described in [`NSScroller.ArrowPosition`](./arrowposition.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/controltint)*