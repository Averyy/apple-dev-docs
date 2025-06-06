# setUser(_:)

**Framework**: AppKit  
**Kind**: method

Sets the font used by default for documents and other text under the user’s control to the specified font.

**Availability**:
- macOS ?+

## Declaration

```swift
class func setUser(_ font: NSFont?)
```

#### Discussion

Specifying `aFont` as `nil` causes the default to be removed from the application domain.

## See Also

- [class func userFont(ofSize: CGFloat) -> NSFont?](nsfont/userfont(ofsize:).md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), in the specified size.
- [class func setUserFixedPitch(NSFont?)](nsfont/setuserfixedpitch(_:).md)
  Sets the font used by default for documents and other text under the user’s control, when that font should be fixed-pitch, to the specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/setuser(_:))*