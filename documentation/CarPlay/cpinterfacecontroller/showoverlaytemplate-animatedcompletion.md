# showOverlayTemplate(_:animated:completion:)

**Framework**: CarPlay  
**Kind**: method

Show a template as an overlay over the current template hierarchy. Only one overlay template may be shown at a time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func showOverlayTemplate(_ templateToShow: CPTemplate, animated: Bool) async throws -> Bool
```

#### Discussion

> **Note**: Supported template types: @c CPVoiceControlTemplate

The completion block will be called after the template has been shown. If the template was shown successfully, the boolean parameter will be YES. Otherwise, the boolean parameter will be NO and an @c NSError will be provided describing the failure.

> **Note**: If the template is not successfully shown AND no completion block is specified, an exception will be thrown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/showoverlaytemplate(_:animated:completion:))*