# alternateIconName

**Framework**: UIKit  
**Kind**: property

The name of the icon the system displays for the app.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var alternateIconName: String? { get }
```

#### Discussion

When the system is displaying one of your app’s alternate icons, the value of this property is the name of the alternate icon (from your app’s `Info.plist` file). When the system is displaying your app’s primary icon, the value of this property is `nil`.

## See Also

- [var supportsAlternateIcons: Bool](uiapplication/supportsalternateicons.md)
  A Boolean value that indicates whether the app is allowed to change its icon.
- [func setAlternateIconName(String?, completionHandler: (((any Error)?) -> Void)?)](uiapplication/setalternateiconname(_:completionhandler:).md)
  Changes the icon the system displays for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/alternateiconname)*