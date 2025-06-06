# effectiveAppearance

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The appearance that will be used when the receiver is drawn onscreen, in an `NSAppearance` object. (read-only)

**Availability**:
- macOS 10.9+

## Declaration

```swift
var effectiveAppearance: NSAppearance { get }
```

#### Discussion

The default value for this property is provided by the nearest ancestor of the receiver that has set an appearance.

You can use this property to ensure that an offscreen view sets the appropriate current appearance when it draws onscreen.

## See Also

- [Choosing a Specific Appearance for Your macOS App](choosing-a-specific-appearance-for-your-macos-app.md)
  Adopt a specific appearance for your windows, views, or app when it is inappropriate to support both light and dark variants.
- [var appearance: NSAppearance?](nsappearancecustomization/appearance.md)
  The appearance of the receiver, in an `NSAppearance` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearancecustomization/effectiveappearance)*