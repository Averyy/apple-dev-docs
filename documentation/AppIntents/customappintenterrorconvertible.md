# CustomAppIntentErrorConvertible

**Framework**: App Intents  
**Kind**: protocol

A type that the system automatically converts to an app intent error.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol CustomAppIntentErrorConvertible
```

#### Overview

Conform your custom type to this protocol when you need full control over the [`AppIntentError`](appintenterror.md) that the system produces — including the error kind and localized description. When you throw a conforming error from a method such as [`perform()`](appintent/perform().md) or [`entities(for:)`](entityquery/entities(for:).md), the framework reads the [`appIntentError`](customappintenterrorconvertible/appintenterror.md) property and uses it directly.

If an error conforms to both [`CustomLocalizedStringResourceConvertible`](https://developer.apple.com/documentation/Foundation/CustomLocalizedStringResourceConvertible) and [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md), the system uses only [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md).

## Topics

### Instance Properties
- [var appIntentError: AppIntentError](customappintenterrorconvertible/appintenterror.md)

## See Also

- [struct AppIntentError](appintenterror.md)
  An error that indicates a problem occurred while performing an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/customappintenterrorconvertible)*