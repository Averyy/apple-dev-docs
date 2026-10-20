# MACaptionAppearanceCopySelectedLanguages(_:)

**Framework**: Media Accessibility  
**Kind**: func  
**Role**: Function

Returns the preferred caption languages.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceCopySelectedLanguages(_ domain: MACaptionAppearanceDomain) -> Unmanaged<CFArray>
```

```c
extern CFArrayRefMACaptionAppearanceCopySelectedLanguages(MACaptionAppearanceDomain domain);
```

#### Return Value

An ordered array of preferred canonical language identifiers.

#### Discussion

Languages added using the [`MACaptionAppearanceAddSelectedLanguage(_:_:)`](./macaptionappearanceaddselectedlanguage%28_,_%29.md) function are normalized. As a result, the contents of the returned array may have slightly different strings from those passed into [`MACaptionAppearanceAddSelectedLanguage(_:_:)`](./macaptionappearanceaddselectedlanguage%28_,_%29.md).

## Parameters

- `domain`: The domain to retrieve the preference value from. See [`MACaptionAppearanceDomain`](./macaptionappearancedomain.md). Pass [`MACaptionAppearanceDomain.user`](./macaptionappearancedomain/user.md) unless the system defaults are needed for comparison.

## See Also

### Language settings
- [func MACaptionAppearanceAddSelectedLanguage(MACaptionAppearanceDomain, CFString) -> Bool](./macaptionappearanceaddselectedlanguage%28_,_%29.md)
  Adds a preference for caption language to the stack of languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearancecopyselectedlanguages(_:))*