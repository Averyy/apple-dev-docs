# userInterfaceLanguage

**Framework**: ProximityReader  
**Kind**: property

The language to use when localizing the user interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var userInterfaceLanguage: Locale.Language?
```

#### Discussion

Setting this attribute only affects customer facing elements, screen elements, or audio targeted at the merchant (device owner) remains set to the language defined in the system settings. When you set this option to `nil`, the framework uses the person’s preferred language defined in System Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest/userinterfacelanguage)*