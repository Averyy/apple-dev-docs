# MACaptionAppearanceIsCustomized(_:)

**Framework**: Media Accessibility  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func MACaptionAppearanceIsCustomized(_ domain: MACaptionAppearanceDomain) -> Bool
```

#### Return Value

A boolean indicating if the currently-active style has been customized by the user

#### Discussion

Provides a boolean indicating if the currently-active style has been customized by the user. This is useful for some clients who may need different fallback strategies for customized styles vs system-default styles.

## Parameters

- `domain`: Preference domain, see  @link MACaptionAppearanceDomain @/link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/macaptionappearanceiscustomized(_:))*