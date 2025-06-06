# NSMatrixDelegate

**Framework**: AppKit  
**Kind**: protocol

The `NSMatrixDelegate` protocol defines the optional methods implemented by delegates of `NSMatrix` objects.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSMatrixDelegate : NSControlTextEditingDelegate
```

#### Overview

This protocol simply adopts the `NSControlTextEditingDelegate` protocol, adding no additional methods. See [`NSControlTextEditingDelegate`](nscontroltexteditingdelegate.md) for more information.

## Relationships

### Inherits From
- [NSControlTextEditingDelegate](nscontroltexteditingdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Matrix Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Matrix/Matrix.html#//apple_ref/doc/uid/10000022i)
- [var delegate: (any NSMatrixDelegate)?](nsmatrix/delegate.md)
  The delegate for messages from the field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrixdelegate)*