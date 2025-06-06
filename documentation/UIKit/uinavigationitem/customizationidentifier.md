# customizationIdentifier

**Framework**: UIKit  
**Kind**: property

A globally unique string that enables user customization of the navigation bar layout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var customizationIdentifier: String? { get set }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

Set a customization identifier to support a personalized navigation bar layout experience. When you assign a string to this property, UIKit allows people to customize the layout of the items in the navigation bar by choosing the customize option in the overflow menu. UIKit automatically saves and restores this custom layout across app launches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/customizationidentifier)*