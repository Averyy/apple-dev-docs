# localizationCode

**Framework**: Core HID  
**Kind**: property

A device localization code that specifies the HID compliant localization code.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let localizationCode: HIDDeviceLocalizationCode?
```

#### Discussion

The localization code can specify the specific format a device is localized. For example, a Japanese (JIS) keyboard should declare the [`HIDDeviceLocalizationCode.japan`](hiddevicelocalizationcode/japan.md) localization code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties/localizationcode)*