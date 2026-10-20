# bestResolution

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

When capturing the window, return the best image resolution. The returned image size may be different than the screen size.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var bestResolution: CGWindowImageOption { get }
```

```c
kCGWindowImageBestResolution
```

## See Also

### Type Properties
- [static var boundsIgnoreFraming: CGWindowImageOption](./boundsignoreframing.md)
- [static var nominalResolution: CGWindowImageOption](./nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [static var onlyShadows: CGWindowImageOption](./onlyshadows.md)
- [static var shouldBeOpaque: CGWindowImageOption](./shouldbeopaque.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/bestresolution)*