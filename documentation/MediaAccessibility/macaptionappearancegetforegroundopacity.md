# MACaptionAppearanceGetForegroundOpacity(_:_:)

**Framework**: Media Accessibility  
**Kind**: func

Returns the preference for text opacity.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceGetForegroundOpacity(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat
```

#### Return Value

The float value, ranging from `0.0` to `1.0`, representing the opacity of the color for text opacity.

## Parameters

- `domain`: The domain to retrieve the preference value from. See  . Pass   unless the system defaults are needed for comparison.
- `behavior`: A pointer to memory. On return, this memory holds the caption appearance behavior for this preference setting. For possible values see  . Pass   when you do not need the behavior setting.

## See Also

- [func MACaptionAppearanceCopyFontDescriptorForStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?, MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>](macaptionappearancecopyfontdescriptorforstyle(_:_:_:).md)
  Returns the preferred font for the specified style of type.
- [func MACaptionAppearanceCopyForegroundColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](macaptionappearancecopyforegroundcolor(_:_:).md)
  Returns the preference for text color.
- [func MACaptionAppearanceGetRelativeCharacterSize(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetrelativecharactersize(_:_:).md)
  Returns the preference for font scaling.
- [func MACaptionAppearanceGetTextEdgeStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> MACaptionAppearanceTextEdgeStyle](macaptionappearancegettextedgestyle(_:_:).md)
  Returns the preference for text edge style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancegetforegroundopacity(_:_:))*