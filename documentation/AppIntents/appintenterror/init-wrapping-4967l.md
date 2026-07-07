# init(wrapping:)

**Framework**: App Intents  
**Kind**: init

Creates an error by wrapping an existing localized error.

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
init(wrapping error: some CustomLocalizedStringResourceConvertible & Error)
```

#### Discussion

Conform your custom `Error` to [`CustomLocalizedStringResourceConvertible`](https://developer.apple.com/documentation/Foundation/CustomLocalizedStringResourceConvertible) to provide a localized description of the error.

The system calls this initializer for errors thrown from [`perform()`](appintent/perform().md) that conform to `CustomLocalizedStringResourceConvertible`.

If the error conforms to both `CustomLocalizedStringResourceConvertible` and [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md), the system uses only [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md).

## Parameters

- `error`: The error to wrap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/init(wrapping:)-4967l)*