# kCTFontVariationAxisHiddenKey

**Framework**: Core Text  
**Kind**: var

The key to find out if the axis is hidden.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let kCTFontVariationAxisHiddenKey: CFString
```

#### Discussion

This key contains a [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) value that is [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) when the font designer recommends the axis not be exposed directly to end users in application interfaces.

Reasons for setting this flag might include that the axis is intended only for programmatic interaction, or is intended for font-internal use by the font developer.

## See Also

- [let kCTFontVariationAxisIdentifierKey: CFString](kctfontvariationaxisidentifierkey.md)
  Key to get the variation axis identifier.
- [let kCTFontVariationAxisMinimumValueKey: CFString](kctfontvariationaxisminimumvaluekey.md)
  Key to get the variation axis minimum value.
- [let kCTFontVariationAxisMaximumValueKey: CFString](kctfontvariationaxismaximumvaluekey.md)
  Key to get the variation axis maximum value.
- [let kCTFontVariationAxisDefaultValueKey: CFString](kctfontvariationaxisdefaultvaluekey.md)
  Key to get the variation axis default value.
- [let kCTFontVariationAxisNameKey: CFString](kctfontvariationaxisnamekey.md)
  Key to get the localized variation axis name string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontvariationaxishiddenkey)*