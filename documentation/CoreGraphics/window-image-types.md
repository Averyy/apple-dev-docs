# Window Image Types

**Framework**: Core Graphics

Specifies the options for capturing an image of a window.

## Topics

### Constants
- [static var boundsIgnoreFraming: CGWindowImageOption](cgwindowimageoption/boundsignoreframing.md)
- [static var shouldBeOpaque: CGWindowImageOption](cgwindowimageoption/shouldbeopaque.md)
- [static var onlyShadows: CGWindowImageOption](cgwindowimageoption/onlyshadows.md)
- [static var bestResolution: CGWindowImageOption](cgwindowimageoption/bestresolution.md)
  When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [static var nominalResolution: CGWindowImageOption](cgwindowimageoption/nominalresolution.md)
  When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.

## See Also

- [Window Sharing Constants](window-sharing-constants.md)
  Specifies whether and how windows are shared between applications.
- [Backing Store Types](backing-store-types.md)
  Specifies how the window device buffers drawing commands.
- [Window List Option Constants](window-list-option-constants.md)
  Specifies which windows in the current user session to include in a generated list.
- [CGWindowID Encoding Type](cgwindowid-encoding-type.md)
  Defines the encoding type for window IDs.
- [Null Window](null-window.md)
  Defines a guaranteed invalid window ID.
- [Window Sharing Encoding Type](window-sharing-encoding-type.md)
  Defines the encoding type for window sharing values.
- [Window Backing Encoding Type](window-backing-encoding-type.md)
  Defines the encoding type for window backing types.
- [Required Window List Keys](required-window-list-keys.md)
  The keys that are guaranteed to be available in a window’s information dictionary.
- [Optional Window List Keys](optional-window-list-keys.md)
  The keys that may optionally be available inside a window’s information dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/window-image-types)*