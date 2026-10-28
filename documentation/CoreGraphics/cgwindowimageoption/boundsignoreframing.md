# boundsIgnoreFraming

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var boundsIgnoreFraming: CGWindowImageOption { get }
```

```c
kCGWindowImageBoundsIgnoreFraming
```

## Discussion

When the requested capture rectangle is [`CGRectNull`](../cgrectnull.md), using this option captures the window area only and does not capture the area occupied by any window framing effects.

## See Also

### Type Properties
- [static var bestResolution: CGWindowImageOption](./bestresolution.md)
  When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [static var nominalResolution: CGWindowImageOption](./nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [static var onlyShadows: CGWindowImageOption](./onlyshadows.md)
- [static var shouldBeOpaque: CGWindowImageOption](./shouldbeopaque.md)
- [kCGWindowImageDefault](./kcgwindowimagedefault.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/boundsignoreframing)*