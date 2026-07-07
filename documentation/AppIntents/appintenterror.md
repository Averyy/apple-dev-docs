# AppIntentError

**Framework**: App Intents  
**Kind**: struct

An error that indicates a problem occurred while performing an app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct AppIntentError
```

#### Overview

When your app intent encounters an error during execution, throw an `AppIntentError` to communicate structured failure information to the system. Apple Intelligence, Siri, and Shortcuts use this information to determine the appropriate response — such as prompting a person, retrying the operation, or reporting the failure.

You can create an `AppIntentError` in several ways:

- **Predefined errors**: Use values from [`AppIntentError.PermissionRequired`](appintenterror/permissionrequired.md), [`AppIntentError.UserActionRequired`](appintenterror/useractionrequired.md), or [`AppIntentError.Unrecoverable`](appintenterror/unrecoverable.md) for common failure scenarios that the system already knows how to handle.
- **Wrapping a custom error**: If your error type conforms to [`CustomLocalizedStringResourceConvertible`](https://developer.apple.com/documentation/Foundation/CustomLocalizedStringResourceConvertible), pass it to `init(wrapping:)` to provide a localized description.
- **Description string**: Create an error with a localized description directly from a [`LocalizedStringResource`](https://developer.apple.com/documentation/Foundation/LocalizedStringResource) and pass it to [`init(description:)`](appintenterror/init(description:).md).

The recommended approach for most apps is to define an error enumeration that conforms to `CustomLocalizedStringResourceConvertible` and throw it from your intent's `AppIntent/perform()`` method. The framework automatically wraps conforming errors into an `AppIntentError` with the localized description you provide.

## Topics

### Getting the error codes
- [static var restartPerform: AppIntentError](appintenterror/restartperform.md)
### Initializers
- [init(description: LocalizedStringResource)](appintenterror/init(description:).md)
  Creates an error with a localized description.
- [init(predefinedError: AppIntentError, description: LocalizedStringResource)](appintenterror/init(predefinederror:description:).md)
  Creates an error from a predefined error with a custom localized description.
- [init(wrapping: some CustomAppIntentErrorConvertible)](appintenterror/init(wrapping:)-2lmed.md)
  Creates an error from a custom app intent convertible value.
- [init(wrapping: some CustomLocalizedStringResourceConvertible & Error)](appintenterror/init(wrapping:)-4967l.md)
  Creates an error by wrapping an existing localized error.
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
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol CustomAppIntentErrorConvertible](customappintenterrorconvertible.md)
  A type that the system automatically converts to an app intent error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror)*