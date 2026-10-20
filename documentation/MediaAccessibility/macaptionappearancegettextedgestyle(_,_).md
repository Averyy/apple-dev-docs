# MACaptionAppearanceGetTextEdgeStyle(_:_:)

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

Returns the preference for text edge style.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceGetTextEdgeStyle(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> MACaptionAppearanceTextEdgeStyle
```

```c
extern MACaptionAppearanceTextEdgeStyle MACaptionAppearanceGetTextEdgeStyle(MACaptionAppearanceDomain domain, MACaptionAppearanceBehavior *behavior);
```

#### Return Value

The preferred text edge style, such as Raised or Drop Shadow. See [`MACaptionAppearanceTextEdgeStyle`](./macaptionappearancetextedgestyle.md).

## Parameters

- `domain`: The domain to retrieve the preference value from. See [`MACaptionAppearanceDomain`](./macaptionappearancedomain.md). Pass [`MACaptionAppearanceDomain.user`](./macaptionappearancedomain/user.md) unless the system defaults are needed for comparison.
- `behavior`: A pointer to memory. On return, this memory holds the caption appearance behavior for this preference setting. For possible values see [`MACaptionAppearanceBehavior`](./macaptionappearancebehavior.md). Pass `NULL` when you do not need the behavior setting.

## See Also

### Text settings
- [func MACaptionAppearanceCopyFontDescriptorForStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?, MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>](./macaptionappearancecopyfontdescriptorforstyle%28_,_,_%29.md)
  Returns the preferred font for the specified style of type.
- [func MACaptionAppearanceCopyForegroundColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](./macaptionappearancecopyforegroundcolor%28_,_%29.md)
  Returns the preference for text color.
- [func MACaptionAppearanceGetForegroundOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](./macaptionappearancegetforegroundopacity%28_,_%29.md)
  Returns the preference for text opacity.
- [func MACaptionAppearanceGetRelativeCharacterSize(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](./macaptionappearancegetrelativecharactersize%28_,_%29.md)
  Returns the preference for font scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancegettextedgestyle(_:_:))*