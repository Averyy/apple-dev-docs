# AccessibilitySettings.Feature

**Framework**: Accessibility  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AXSettingsFeature : NSInteger;
```

## Topics

### Audio features
- [AccessibilitySettings.Feature.personalVoiceAllowAppsToRequestToUse](./feature/personalvoiceallowappstorequesttouse.md)
  A constant for opening the Settings app to the setting for Personal Voice > Allow Apps to Request to Use.
### Accessibility feature structure creation
- [init?(rawValue: Int)](./feature/init%28rawvalue%29.md)
### Enumeration Cases
- [AccessibilitySettings.Feature.allowAppsToAddAudioToCalls](./feature/allowappstoaddaudiotocalls.md)
- [AccessibilitySettings.Feature.assistiveTouch](./feature/assistivetouch.md)
- [AccessibilitySettings.Feature.assistiveTouchDevices](./feature/assistivetouchdevices.md)
- [AccessibilitySettings.Feature.captionStyles](./feature/captionstyles.md)
- [AccessibilitySettings.Feature.dwellControl](./feature/dwellcontrol.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Opening the Settings app
- [static func openSettings(for: AccessibilitySettings.Feature) async throws](./opensettings%28for%29.md)
  Opens the Settings app to a specific section of Accessibility settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/feature)*