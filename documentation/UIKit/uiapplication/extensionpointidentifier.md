# UIApplication.ExtensionPointIdentifier

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A structure that identifies types of extensions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct ExtensionPointIdentifier
```

```c
typedef NSString * UIApplicationExtensionPointIdentifier;
```

## Topics

### Constants
- [static let keyboard: UIApplication.ExtensionPointIdentifier](./extensionpointidentifier/keyboard.md)
  The identifier for custom keyboards.
### Initializers
- [init(rawValue: String)](./extensionpointidentifier/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Disallowing specified app extension types
- [func application(UIApplication, shouldAllowExtensionPointIdentifier: UIApplication.ExtensionPointIdentifier) -> Bool](../uiapplicationdelegate/application%28_,shouldallowextensionpointidentifier%29.md)
  Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [static let keyboard: UIApplication.ExtensionPointIdentifier](./extensionpointidentifier/keyboard.md)
  The identifier for custom keyboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/extensionpointidentifier)*