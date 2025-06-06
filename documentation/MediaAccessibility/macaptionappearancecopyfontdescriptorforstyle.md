# MACaptionAppearanceCopyFontDescriptorForStyle(_:_:_:)

**Framework**: Media Accessibility  
**Kind**: func

Returns the preferred font for the specified style of type.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceCopyFontDescriptorForStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?, _ fontStyle: MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>
```

#### Return Value

The name of the preferred font for the specified style.

## Parameters

- `domain`: The domain to retrieve the preference value from. See  . Pass   unless the system defaults are needed for comparison.
- `behavior`: A pointer to memory. On return, this memory holds the caption appearance behavior for this preference setting. For possible values see  . Pass   when you do not need the behavior setting.
- `fontStyle`: A font style, such as cursive or small caps, see  .

## See Also

- [func MACaptionAppearanceCopyForegroundColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](macaptionappearancecopyforegroundcolor(_:_:).md)
  Returns the preference for text color.
- [func MACaptionAppearanceGetForegroundOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetforegroundopacity(_:_:).md)
  Returns the preference for text opacity.
- [func MACaptionAppearanceGetRelativeCharacterSize(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetrelativecharactersize(_:_:).md)
  Returns the preference for font scaling.
- [func MACaptionAppearanceGetTextEdgeStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> MACaptionAppearanceTextEdgeStyle](macaptionappearancegettextedgestyle(_:_:).md)
  Returns the preference for text edge style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyfontdescriptorforstyle(_:_:_:))*