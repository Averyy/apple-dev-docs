# init(wrapping:)

**Framework**: App Intents  
**Kind**: init

Creates an error by wrapping an existing localized error.

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
init(wrapping error: some CustomLocalizedStringResourceConvertible & Error)
```

#### Discussion

Conform your custom `Error` to [`CustomLocalizedStringResourceConvertible`](https://developer.apple.com/documentation/foundation/customlocalizedstringresourceconvertible) to provide a localized description of the error.

The system calls this initializer for errors thrown from [`perform()`](appintent/perform().md) that conform to `CustomLocalizedStringResourceConvertible`.

If the error conforms to both `CustomLocalizedStringResourceConvertible` and [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md), the system uses only [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md).

## Parameters

- `error`: The error to wrap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/init(wrapping:)-4967l)*