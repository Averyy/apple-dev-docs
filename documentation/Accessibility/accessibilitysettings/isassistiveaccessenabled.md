# isAssistiveAccessEnabled

**Framework**: Accessibility  
**Kind**: property

A Boolean value that indicates whether Assistive Access is running.

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
static var isAssistiveAccessEnabled: Bool { get }
```

## Mentions

- [Optimizing your app for Assistive Access](optimizing-your-app-for-assistive-access.md)

#### Discussion

The value of this property doesn’t change during a process’s lifetime, so it isn’t necessary to observe changes.

## See Also

- [var accessibilityAssistiveAccessEnabled: Bool { get }](../SwiftUI/EnvironmentValues/accessibilityAssistiveAccessEnabled.md)
  A Boolean value that indicates whether Assistive Access is in use.
- [Assistive Access](assistive-access.md)
  A mode that tailors the iOS and iPadOS experience for people with cognitive disabilities.
- [UISupportsFullScreenInAssistiveAccess](../BundleResources/Information-Property-List/UISupportsFullScreenInAssistiveAccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/isassistiveaccessenabled)*