# localizedName(forFamily:face:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a localized string with the name of the specified font family and face, if one exists.

**Availability**:
- macOS

## Declaration

```swift
func localizedName(forFamily family: String, face faceKey: String?) -> String
```

```objc
- (NSString *) localizedNameForFamily:(NSString *) family face:(NSString *) faceKey;
```

## Return Value

A localized string with the name of the specified font family and face, or, if `face` is `nil`, the font family only.

## Discussion

The user’s locale is determined from the user’s `NSLanguages` default setting. The method also loads the localized strings for the font, if they aren’t already loaded.

## Parameters

- `family`: The font family, for example, `@"Times"`.
- `faceKey`: The font face, for example, `@"Roman"`.

## See Also

### Setting and Examining the Selected Font
- [func setSelectedFont(NSFont, isMultiple: Bool)](./setselectedfont%28_,ismultiple%29.md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var selectedFont: NSFont?](./selectedfont.md)
  The currently selected font object.
- [var isMultiple: Bool](./ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func sendAction() -> Bool](./sendaction%28%29.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/localizedname(forfamily:face:))*