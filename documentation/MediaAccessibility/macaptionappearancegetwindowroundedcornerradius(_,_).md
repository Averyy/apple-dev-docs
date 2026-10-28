# MACaptionAppearanceGetWindowRoundedCornerRadius(_:_:)

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

Returns the radius of the caption window’s corners.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceGetWindowRoundedCornerRadius(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat
```

```c
extern CGFloat MACaptionAppearanceGetWindowRoundedCornerRadius(MACaptionAppearanceDomain domain, MACaptionAppearanceBehavior *behavior);
```

## Return Value

The system setting for the caption window’s corner radius.

## Discussion

The rounded corners of the caption window are not customizable within the Accessibility preferences and do not change based on text size.

## Parameters

- `domain`: The domain to retrieve the preference value from. See [`MACaptionAppearanceDomain`](./macaptionappearancedomain.md). Pass [`MACaptionAppearanceDomain.user`](./macaptionappearancedomain/user.md) unless the system defaults are needed for comparison.
- `behavior`: A pointer to memory. On return, this memory holds the caption appearance behavior for this preference setting. For possible values see [`MACaptionAppearanceBehavior`](./macaptionappearancebehavior.md). Pass `NULL` when you do not need the behavior setting.

## See Also

### Caption window settings
- [func MACaptionAppearanceCopyWindowColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](./macaptionappearancecopywindowcolor%28_,_%29.md)
  Returns the preference for the caption window’s color.
- [func MACaptionAppearanceGetWindowOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](./macaptionappearancegetwindowopacity%28_,_%29.md)
  Returns the preference for the overlay’s opacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancegetwindowroundedcornerradius(_:_:))*