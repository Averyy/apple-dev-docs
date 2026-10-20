# grayscaleStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that UIKit posts when the system’s Grayscale setting changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let grayscaleStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIAccessibilityGrayscaleStatusDidChangeNotification;
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

### Colors
- [static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name](./darkersystemcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [static let invertColorsStatusDidChangeNotification: NSNotification.Name](./invertcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the settings for inverted colors change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/grayscalestatusdidchangenotification)*