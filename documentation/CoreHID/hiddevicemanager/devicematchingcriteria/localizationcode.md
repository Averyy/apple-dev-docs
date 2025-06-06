# localizationCode

**Framework**: Core HID  
**Kind**: property

A localization code that specifies the HID compliant localization code.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var localizationCode: HIDDeviceLocalizationCode?
```

#### Discussion

The localization code can specify for which specific format the device is localized. For example, a Japanese (JIS) keyboard declares the [`HIDDeviceLocalizationCode.japan`](hiddevicelocalizationcode/japan.md) localization code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria/localizationcode)*