# shouldBeOpaque

**Framework**: Core Graphics  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var shouldBeOpaque: CGWindowImageOption { get }
```

#### Discussion

When capturing the window, partially transparent areas are backed by a solid white color so that the resulting image is fully opaque. You can combine this option with other options.

## See Also

- [static var bestResolution: CGWindowImageOption](cgwindowimageoption/bestresolution.md)
  When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [static var boundsIgnoreFraming: CGWindowImageOption](cgwindowimageoption/boundsignoreframing.md)
- [static var nominalResolution: CGWindowImageOption](cgwindowimageoption/nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [static var onlyShadows: CGWindowImageOption](cgwindowimageoption/onlyshadows.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/shouldbeopaque)*