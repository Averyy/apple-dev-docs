# onlyShadows

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var onlyShadows: CGWindowImageOption { get }
```

```c
kCGWindowImageOnlyShadows
```

## Discussion

When capturing the window, only the shadow effects are captured.

## See Also

### Type Properties
- [static var bestResolution: CGWindowImageOption](./bestresolution.md)
  When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [static var boundsIgnoreFraming: CGWindowImageOption](./boundsignoreframing.md)
- [static var nominalResolution: CGWindowImageOption](./nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [static var shouldBeOpaque: CGWindowImageOption](./shouldbeopaque.md)
- [kCGWindowImageDefault](./kcgwindowimagedefault.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/onlyshadows)*