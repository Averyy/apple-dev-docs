# isApplicationAccessibilityEnabled

**Framework**: Accessibility  
**Kind**: property

Returns whether application accessibility is currently enabled for this process.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var isApplicationAccessibilityEnabled: Bool { get }
```

#### Discussion

Returns `YES` when at least one assistive technology — such as VoiceOver, Switch Control, Voice Control, or Full Keyboard Access — has requested access to this app’s accessibility information. Apps can use this signal to avoid building expensive accessibility data when no assistive technology is consuming it.

The value can change during a process’s lifetime; observe `AXApplicationAccessibilityEnabledDidChangeNotification` to react to changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/isapplicationaccessibilityenabled)*