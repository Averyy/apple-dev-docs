# boldTextStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that UIKit posts when the system’s Bold Text setting changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let boldTextStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIAccessibilityBoldTextStatusDidChangeNotification;
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Text
- [static let closedCaptioningStatusDidChangeNotification: NSNotification.Name](./closedcaptioningstatusdidchangenotification.md)
  A notification that UIKit posts when the setting for Closed Captions + SDH changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/boldtextstatusdidchangenotification)*