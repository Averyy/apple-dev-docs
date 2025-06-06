# keyboard

**Framework**: UIKit  
**Kind**: property

The identifier for custom keyboards.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let keyboard: UIApplication.ExtensionPointIdentifier
```

#### Discussion

To reject the use of custom keyboards in your app, specify this constant in your implementation of the [`application(_:shouldAllowExtensionPointIdentifier:)`](uiapplicationdelegate/application(_:shouldallowextensionpointidentifier:).md) delegate method.

## See Also

- [func application(UIApplication, shouldAllowExtensionPointIdentifier: UIApplication.ExtensionPointIdentifier) -> Bool](uiapplicationdelegate/application(_:shouldallowextensionpointidentifier:).md)
  Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [UIApplication.ExtensionPointIdentifier](uiapplication/extensionpointidentifier.md)
  A structure that identifies types of extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/extensionpointidentifier/keyboard)*