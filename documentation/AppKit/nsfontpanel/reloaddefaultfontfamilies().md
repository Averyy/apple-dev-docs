# reloadDefaultFontFamilies()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Triggers a reload to the default state, so that the delegate is called.

**Availability**:
- macOS

## Declaration

```swift
func reloadDefaultFontFamilies()
```

```objc
- (void) reloadDefaultFontFamilies;
```

## Discussion

This reloading provides the delegate opportunity to scrutinize the default list of fonts to be displayed in the panel.

## See Also

### Enabling Font Changes
- [var isEnabled: Bool](./isenabled.md)
  A Boolean that shows whether the receiver’s Set button is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/reloaddefaultfontfamilies())*