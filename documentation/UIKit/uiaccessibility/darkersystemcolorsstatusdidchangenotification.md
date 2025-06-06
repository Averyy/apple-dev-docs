# darkerSystemColorsStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that UIKit posts when the system’s Increase Contrast setting changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

## See Also

- [static let grayscaleStatusDidChangeNotification: NSNotification.Name](uiaccessibility/grayscalestatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Grayscale setting changes.
- [static let invertColorsStatusDidChangeNotification: NSNotification.Name](uiaccessibility/invertcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the settings for inverted colors change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/darkersystemcolorsstatusdidchangenotification)*