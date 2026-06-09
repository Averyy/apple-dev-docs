# hideOverlayTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Dismiss the current overlay template, optionally animating the dismissal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func hideOverlayTemplate(animated: Bool) async throws -> Bool
```

#### Discussion

> **Note**: If there is no current overlay template, this method will have no effect.

The completion block will be called after the template has been dismissed. If the template was dismissed successfully, the boolean parameter will be YES. Otherwise, the boolean parameter will be NO and an @c NSError will be provided describing the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/hideoverlaytemplate(animated:completion:))*