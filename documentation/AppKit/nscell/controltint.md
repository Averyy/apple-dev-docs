# controlTint

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s control tint.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

> **Deprecated**: The controlTint property is not respected on 10.14 and later. For custom cells, use +[NSColor controlAccentColor] to respect the user's preferred accent color when drawing.

## Declaration

```swift
var controlTint: NSControlTint { get set }
```

```objc
@property NSControlTint controlTint;
```

## Discussion

The default value of this property is [`NSControlTint.defaultControlTint`](../nscontroltint/defaultcontroltint.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/controltint)*