# AccessibilitySettings

**Framework**: Accessibility  
**Kind**: struct

A structure for working with accessibility system settings.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct AccessibilitySettings
```

## Topics

### Opening the Settings app
- [static func openSettings(for: AccessibilitySettings.Feature) async throws](accessibilitysettings/opensettings(for:).md)
  Opens the Settings app to a specific section of Accessibility settings.
- [AccessibilitySettings.Feature](accessibilitysettings/feature.md)
  Constants that describe specific Accessibility settings in the Settings app.
### Pausing animated images
- [Animated images](animated-images.md)
  Pause animations in animated images in your app when people turn off the Animated Images setting.
- [static var animatedImagesEnabled: Bool](accessibilitysettings/animatedimagesenabled.md)
  A Boolean value that indicates whether the system setting for playing animated images is on.
- [static var animatedImagesEnabledDidChangeNotification: Notification.Name](accessibilitysettings/animatedimagesenableddidchangenotification.md)
  A notification that posts when the system setting for playing animated images changes.
### Customizing vertical text layout
- [Horizontal text](horizontal-text.md)
  Lay out vertical text horizontally in your app when people turn on the Prefer Horizontal Text setting.
- [static var prefersHorizontalTextLayout: Bool](accessibilitysettings/prefershorizontaltextlayout.md)
  A Boolean value that indicates whether the system setting to prefer horizontal text for languages that support both vertical and horizontal text layout is on.
- [static var prefersHorizontalTextLayoutDidChangeNotification: Notification.Name](accessibilitysettings/prefershorizontaltextlayoutdidchangenotification.md)
  A notification that posts when the system setting to prefer horizontal text for languages that support both vertical and horizontal text layout changes.
### Supporting head-anchored content
- [static var prefersHeadAnchorAlternative: Bool](accessibilitysettings/prefersheadanchoralternative.md)
  A Boolean value that indicates the person’s preference for content that follows their head position.
- [static var prefersHeadAnchorAlternativeDidChangeNotification: Notification.Name](accessibilitysettings/prefersheadanchoralternativedidchangenotification.md)
  A notification that posts when the system setting for head-anchored content changes.
### Reducing animation for text insertion indicators
- [static var prefersNonBlinkingTextInsertionIndicator: Bool](accessibilitysettings/prefersnonblinkingtextinsertionindicator.md)
  A Boolean value that indicates whether the system setting to prefer a nonblinking cursor in editable text fields is on.
- [static let prefersNonBlinkingTextInsertionIndicatorDidChangeNotification: NSNotification.Name](accessibilitysettings/prefersnonblinkingtextinsertionindicatordidchangenotification.md)
  A notification that posts when the system setting to prefer a nonblinking cursor in editable text fields changes.
### Checking if Assistive Access is running
- [static var isAssistiveAccessEnabled: Bool](accessibilitysettings/isassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is running.
### Creating an accessibility settings structure
- [init()](accessibilitysettings/init.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings)*