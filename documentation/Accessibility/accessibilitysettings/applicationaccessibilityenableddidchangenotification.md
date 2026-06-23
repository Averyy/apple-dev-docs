# applicationAccessibilityEnabledDidChangeNotification

**Framework**: Accessibility  
**Kind**: property

Posted when the value returned by `AXApplicationAccessibilityEnabled()` changes.

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
static let applicationAccessibilityEnabledDidChangeNotification: NSNotification.Name
```

#### Discussion

Posted on the main thread. The notification’s `object` is `nil` and its `userInfo` dictionary is empty — clients should re-read `AXApplicationAccessibilityEnabled()` when handling the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/applicationaccessibilityenableddidchangenotification)*