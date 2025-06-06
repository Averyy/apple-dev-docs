# activityViewControllerProvider

**Framework**: UIKit  
**Kind**: property

A closure that provides an activity view controller for sharing the document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var activityViewControllerProvider: (() -> UIActivityViewController)? { get set }
```

#### Discussion

To support sharing, assign a closure that returns a [`UIActivityViewController`](uiactivityviewcontroller.md) that you configure to share the document. When you set this property, a person can share the document by tapping the share button in the navigation item’s title menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties/activityviewcontrollerprovider)*