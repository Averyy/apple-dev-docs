# invertColorsStatusDidChangeNotification

**Framework**: UIKit  
**Kind**: property

A notification that UIKit posts when the settings for inverted colors change.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
static let invertColorsStatusDidChangeNotification: NSNotification.Name
```

#### Discussion

This notification doesn’t include a parameter. Observe this notification using the default notification center.

Use the [`isInvertColorsEnabled`](uiaccessibility/isinvertcolorsenabled.md) function to determine whether the settings for inverted colors are in an enabled state.

## See Also

- [static let darkerSystemColorsStatusDidChangeNotification: NSNotification.Name](uiaccessibility/darkersystemcolorsstatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Increase Contrast setting changes.
- [static let grayscaleStatusDidChangeNotification: NSNotification.Name](uiaccessibility/grayscalestatusdidchangenotification.md)
  A notification that UIKit posts when the system’s Grayscale setting changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/invertcolorsstatusdidchangenotification)*