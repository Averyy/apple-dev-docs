# NSVisualEffectView.BlendingMode.behindWindow

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A mode that blends and blurs the visual effect view with the contents behind the window, such as the desktop or other windows.

**Availability**:
- macOS 10.10+

## Declaration

```swift
case behindWindow
```

```c
NSVisualEffectBlendingModeBehindWindow
```

## Discussion

Views using this blending mode can overlap, and the view lower in the hierarchy “wins”.

## See Also

### Blend Modes
- [NSVisualEffectView.BlendingMode.withinWindow](./withinwindow.md)
  A mode that blends and blurs the visual effect view with contents behind the view in the current window only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum/behindwindow)*