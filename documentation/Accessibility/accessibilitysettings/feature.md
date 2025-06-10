# AccessibilitySettings.Feature

**Framework**: Accessibility  
**Kind**: enum

Constants that describe specific Accessibility settings in the Settings app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum Feature
```

## Topics

### Audio features
- [AccessibilitySettings.Feature.personalVoiceAllowAppsToRequestToUse](accessibilitysettings/feature/personalvoiceallowappstorequesttouse.md)
  A constant for opening the Settings app to the setting for Personal Voice > Allow Apps to Request to Use.
### Accessibility feature structure creation
- [init?(rawValue: Int)](accessibilitysettings/feature/init(rawvalue:).md)
### Enumeration Cases
- [AccessibilitySettings.Feature.allowAppsToAddAudioToCalls](accessibilitysettings/feature/allowappstoaddaudiotocalls.md)
- [AccessibilitySettings.Feature.assistiveTouch](accessibilitysettings/feature/assistivetouch.md)
- [AccessibilitySettings.Feature.assistiveTouchDevices](accessibilitysettings/feature/assistivetouchdevices.md)
- [AccessibilitySettings.Feature.dwellControl](accessibilitysettings/feature/dwellcontrol.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func openSettings(for: AccessibilitySettings.Feature) async throws](accessibilitysettings/opensettings(for:).md)
  Opens the Settings app to a specific section of Accessibility settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/feature)*