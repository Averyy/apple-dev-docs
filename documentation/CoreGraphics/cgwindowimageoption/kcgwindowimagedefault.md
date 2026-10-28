# kCGWindowImageDefault

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
kCGWindowImageDefault
```

## Discussion

When the requested capture rectangle is [`CGRectNull`](../cgrectnull.md), using this option captures the entire window plus the area required to display any framing effects, such as the window’s shadow. This is the default behavior.

## See Also

### Type Properties
- [static var bestResolution: CGWindowImageOption](./bestresolution.md)
  When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [static var boundsIgnoreFraming: CGWindowImageOption](./boundsignoreframing.md)
- [static var nominalResolution: CGWindowImageOption](./nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [static var onlyShadows: CGWindowImageOption](./onlyshadows.md)
- [static var shouldBeOpaque: CGWindowImageOption](./shouldbeopaque.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimagedefault)*