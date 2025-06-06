# application(_:shouldAllowExtensionPointIdentifier:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, shouldAllowExtensionPointIdentifier extensionPointIdentifier: UIApplication.ExtensionPointIdentifier) -> Bool
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

#### Return Value

[`false`](https://developer.apple.com/documentation/swift/false) to disallow use of a specified app extension type, or [`true`](https://developer.apple.com/documentation/swift/true) to allow use of the type.

#### Discussion

You can implement this method to reject a specified type of app extension, based on its extension point identifier, from use in your app. See Extension Point Identifier Constants in [`UIApplication`](uiapplication.md).

If you do not implement this method, all app extension types are available for use in your app.

In iOS 8.0, the only type of app extension you can reject is the custom keyboard. For information on app extensions, see [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Parameters

- `application`: Your shared app object.
- `extensionPointIdentifier`: A constant identifying an extension point.

## See Also

- [UIApplication.ExtensionPointIdentifier](uiapplication/extensionpointidentifier.md)
  A structure that identifies types of extensions.
- [static let keyboard: UIApplication.ExtensionPointIdentifier](uiapplication/extensionpointidentifier/keyboard.md)
  The identifier for custom keyboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldallowextensionpointidentifier:))*