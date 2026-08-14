# UIApplication.ExtensionPointIdentifier

**Framework**: UIKit  
**Kind**: struct

A structure that identifies types of extensions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct ExtensionPointIdentifier
```

## Topics

### Constants
- [static let keyboard: UIApplication.ExtensionPointIdentifier](uiapplication/extensionpointidentifier/keyboard.md)
  The identifier for custom keyboards.
### Initializers
- [init(rawValue: String)](uiapplication/extensionpointidentifier/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func application(UIApplication, shouldAllowExtensionPointIdentifier: UIApplication.ExtensionPointIdentifier) -> Bool](uiapplicationdelegate/application(_:shouldallowextensionpointidentifier:).md)
  Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [static let keyboard: UIApplication.ExtensionPointIdentifier](uiapplication/extensionpointidentifier/keyboard.md)
  The identifier for custom keyboards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/extensionpointidentifier)*