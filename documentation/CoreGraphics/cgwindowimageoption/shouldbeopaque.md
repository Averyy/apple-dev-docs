# shouldBeOpaque

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var shouldBeOpaque: CGWindowImageOption { get }
```

```c
kCGWindowImageShouldBeOpaque
```

#### Discussion

When capturing the window, partially transparent areas are backed by a solid white color so that the resulting image is fully opaque. You can combine this option with other options.

## See Also

### Type Properties
- [static var bestResolution: CGWindowImageOption](./bestresolution.md)
  When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [static var boundsIgnoreFraming: CGWindowImageOption](./boundsignoreframing.md)
- [static var nominalResolution: CGWindowImageOption](./nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [static var onlyShadows: CGWindowImageOption](./onlyshadows.md)
- [kCGWindowImageDefault](./kcgwindowimagedefault.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/shouldbeopaque)*