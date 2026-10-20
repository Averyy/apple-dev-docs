# setUser(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Sets the font used by default for documents and other text under the user’s control to the specified font.

**Availability**:
- macOS

## Declaration

```swift
class func setUser(_ font: NSFont?)
```

```objc
+ (void) setUserFont:(NSFont *) font;
```

#### Discussion

Specifying `aFont` as `nil` causes the default to be removed from the application domain.

## See Also

### Related Documentation
- [class func userFont(ofSize: CGFloat) -> NSFont?](./userfont%28ofsize%29.md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), in the specified size.
### Setting User Fonts
- [class func setUserFixedPitch(NSFont?)](./setuserfixedpitch%28_%29.md)
  Sets the font used by default for documents and other text under the user’s control, when that font should be fixed-pitch, to the specified font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/setuser(_:))*