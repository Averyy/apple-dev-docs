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
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSMatrix](nsmatrix.md)
  A legacy interface for grouping radio buttons or other types of cells together.
- [var delegate: (any NSMatrixDelegate)?](nsmatrix/delegate.md)
  The delegate for messages from the field editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrixdelegate)*