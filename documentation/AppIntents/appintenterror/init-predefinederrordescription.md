# init(predefinedError:description:)

**Framework**: App Intents  
**Kind**: init

Creates an error from a predefined error with a custom localized description.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(predefinedError: AppIntentError, description: LocalizedStringResource)
```

#### Discussion

Use this initializer to create one of the predefined [`AppIntentError`](appintenterror.md) values with a custom message specific to your app’s context.

See the predefined static properties on [`AppIntentError`](appintenterror.md) for the list of accepted values. Passing any other [`AppIntentError`](appintenterror.md) value triggers a runtime failure via `fatalError()`.

## Parameters

- `predefinedError`: The predefined error to throw.
- `description`: A custom localized description of the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/init(predefinederror:description:))*