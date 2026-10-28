# AppIntentError

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

An error that indicates a problem occurred while performing an app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct AppIntentError
```

## Overview

When your app intent encounters an error during execution, throw an `AppIntentError` to communicate structured failure information to the system. Apple Intelligence, Siri, and Shortcuts use this information to determine the appropriate response — such as prompting a person, retrying the operation, or reporting the failure.

You can create an `AppIntentError` in several ways:

- **Predefined errors**: Use values from [`AppIntentError.PermissionRequired`](./appintenterror/permissionrequired.md), [`AppIntentError.UserActionRequired`](./appintenterror/useractionrequired.md), or [`AppIntentError.Unrecoverable`](./appintenterror/unrecoverable.md) for common failure scenarios that the system already knows how to handle.
- **Wrapping a custom error**: If your error type conforms to [`CustomLocalizedStringResourceConvertible`](../Foundation/customlocalizedstringresourceconvertible.md), pass it to [`init(wrapping:)`](./appintenterror/init%28wrapping%29-2lmed.md) to provide a localized description.
- **Description string**: Create an error with a localized description directly from a [`LocalizedStringResource`](../Foundation/localizedstringresource.md) and pass it to [`init(description:)`](./appintenterror/init%28description%29.md).

The recommended approach for most apps is to define an error enumeration that conforms to [`CustomLocalizedStringResourceConvertible`](../Foundation/customlocalizedstringresourceconvertible.md) and throw it from your intent’s [`perform()`](./appintent/perform%28%29.md) method. The framework automatically wraps conforming errors into an `AppIntentError` with the localized description you provide.

## Topics

### Getting the error codes
- [static var restartPerform: AppIntentError](./appintenterror/restartperform.md)
### Initializers
- [init(description: LocalizedStringResource)](./appintenterror/init%28description%29.md)
  Creates an error with a localized description.
- [init(predefinedError: AppIntentError, description: LocalizedStringResource)](./appintenterror/init%28predefinederror,description%29.md)
  Creates an error from a predefined error with a custom localized description.
- [init(wrapping: some CustomAppIntentErrorConvertible)](./appintenterror/init%28wrapping%29-2lmed.md)
  Creates an error from a custom app intent convertible value.
- [init(wrapping: some CustomLocalizedStringResourceConvertible & Error)](./appintenterror/init%28wrapping%29-4967l.md)
  Creates an error by wrapping an existing localized error.
### Enumerations
- [AppIntentError.PermissionRequired](./appintenterror/permissionrequired.md)
  Errors that indicate the app doesn’t have the required permission to perform an action.
- [AppIntentError.Unrecoverable](./appintenterror/unrecoverable.md)
  Unknown or unrecoverable errors that might have occurred due to either a system or user error.
- [AppIntentError.UserActionRequired](./appintenterror/useractionrequired.md)
  Errors that represent a state where a person needs to respond to successfully complete the action.
### Default Implementations
- [CustomLocalizedStringResourceConvertible Implementations](./appintenterror/customlocalizedstringresourceconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/customlocalizedstringresourceconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [protocol CustomAppIntentErrorConvertible](./customappintenterrorconvertible.md)
  A type that the system automatically converts to an app intent error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror)*