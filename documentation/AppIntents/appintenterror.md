# AppIntentError

**Framework**: App Intents  
**Kind**: struct

Errors that your intent-handling code can return to indicate problems while interpreting or executing an app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct AppIntentError
```

## Topics

### Getting the error codes
- [static var restartPerform: AppIntentError](appintenterror/restartperform.md)
### Enumerations
- [AppIntentError.PermissionRequired](appintenterror/permissionrequired.md)
  Errors that indicate the app doesn’t have the required permission to perform an action.
- [AppIntentError.Unrecoverable](appintenterror/unrecoverable.md)
  Unknown or unrecoverable errors that might have occurred due to either a system or user error.
- [AppIntentError.UserActionRequired](appintenterror/useractionrequired.md)
  Errors that represent a state where a person needs to respond to successfully complete the action.
### Default Implementations
- [CustomLocalizedStringResourceConvertible Implementations](appintenterror/customlocalizedstringresourceconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror)*