# hideOverlayTemplate(animated:completion:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Dismiss the current overlay template, optionally animating the dismissal.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func hideOverlayTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)? = nil)
```

```swift
func hideOverlayTemplate(animated: Bool) async throws -> Bool
```

```objc
- (void) hideOverlayTemplateAnimated:(BOOL) animated completion:(void (^)(BOOL success, NSError *error)) completion;
```

#### Discussion

> **Note**: If there is no current overlay template, this method will have no effect.

The completion block will be called after the template has been dismissed. If the template was dismissed successfully, the boolean parameter will be YES. Otherwise, the boolean parameter will be NO and an @c NSError will be provided describing the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/hideoverlaytemplate(animated:completion:))*