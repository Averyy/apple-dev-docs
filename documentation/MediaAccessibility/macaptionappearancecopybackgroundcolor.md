# MACaptionAppearanceCopyBackgroundColor(_:_:)

**Framework**: Media Accessibility  
**Kind**: func

Returns the preference for the text highlight color.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceCopyBackgroundColor(_ domain: MACaptionAppearanceDomain, _ behavior: UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>
```

#### Return Value

The preferred color shown behind the text and above the window color.

## Parameters

- `domain`: The domain to retrieve the preference value from. See  . Pass   unless the system defaults are needed for comparison.
- `behavior`: A pointer to memory. On return, this memory holds the caption appearance behavior for this preference setting. For possible values see  . Pass   when you do not need the behavior setting.

## See Also

- [func MACaptionAppearanceGetBackgroundOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetbackgroundopacity(_:_:).md)
  Returns the preference for the text highlight opacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopybackgroundcolor(_:_:))*