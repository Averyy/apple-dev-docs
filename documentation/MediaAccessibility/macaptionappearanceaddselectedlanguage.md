# MACaptionAppearanceAddSelectedLanguage(_:_:)

**Framework**: Media Accessibility  
**Kind**: func

Adds a preference for caption language to the stack of languages.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func MACaptionAppearanceAddSelectedLanguage(_ domain: MACaptionAppearanceDomain, _ language: CFString) -> Bool
```

#### Return Value

Returns `true` if addition was successful; `false` if an error occurred. Errors are most likely the result of invalid language codes.

#### Discussion

The added language will appear in the array returned by [`MACaptionAppearanceCopySelectedLanguages(_:)`](macaptionappearancecopyselectedlanguages(_:).md). Call the `MACaptionAppearanceAddSelectedLanguage` function anytime a user selects a specific captioning language from a pop-up menu or other UI affordance. For example, an AVFoundation client may execute the following code:

```objc
 // in response to a user selection, make the selection effective
-[AVPlayerItem selectMediaOption:legibleOption inMediaSelectionGroup:legibleGroup];
 
// now update system-wide captioning preferences by registering the added language
MACaptionAppearanceAddSelectedLanguage(kMACaptionAppearanceDomainUser, (CFStringRef)[[legibleOption locale] localeIdentifier]);
```

## Parameters

- `domain`: The domain to retrieve the preference value from. See  . Pass   unless the system defaults are needed for comparison.
- `language`: A canonical language identifier (see  ) of the preferred caption language.

## See Also

- [func MACaptionAppearanceCopySelectedLanguages(MACaptionAppearanceDomain) -> Unmanaged<CFArray>](macaptionappearancecopyselectedlanguages(_:).md)
  Returns the preferred caption languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearanceaddselectedlanguage(_:_:))*