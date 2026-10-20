# applicationAccessibilityEnabledDidChangeNotification

**Framework**: Accessibility  
**Kind**: property  
**Role**: Type Property

Posted when the value returned by `AXApplicationAccessibilityEnabled()` changes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let applicationAccessibilityEnabledDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AXApplicationAccessibilityEnabledDidChangeNotification;
```

#### Discussion

Posted on the main thread. The notification’s `object` is `nil` and its `userInfo` dictionary is empty — clients should re-read `AXApplicationAccessibilityEnabled()` when handling the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/applicationaccessibilityenableddidchangenotification)*