# appearance

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The appearance of the receiver, in an `NSAppearance` object.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var appearance: NSAppearance? { get set }
```

## Mentions

- [Choosing a Specific Appearance for Your macOS App](choosing-a-specific-appearance-for-your-macos-app.md)

#### Discussion

The default value for this property is `nil`, which means that the receiver uses the appearance it inherits from the nearest ancestor that has set an appearance. When you set `appearance` to a non-`nil` value, the receiver and the views it contains use the specified appearance.

## See Also

- [Choosing a Specific Appearance for Your macOS App](choosing-a-specific-appearance-for-your-macos-app.md)
  Adopt a specific appearance for your windows, views, or app when it is inappropriate to support both light and dark variants.
- [var effectiveAppearance: NSAppearance](nsappearancecustomization/effectiveappearance.md)
  The appearance that will be used when the receiver is drawn onscreen, in an `NSAppearance` object. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsappearancecustomization/appearance)*