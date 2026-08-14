# init(wrapping:)

**Framework**: App Intents  
**Kind**: init

Creates an error from a custom app intent convertible value.

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
init(wrapping convertible: some CustomAppIntentErrorConvertible)
```

#### Discussion

The system calls this initializer for errors thrown from [`perform()`](appintent/perform().md) that conform to [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md).

If the error conforms to both [`CustomLocalizedStringResourceConvertible`](https://developer.apple.com/documentation/foundation/customlocalizedstringresourceconvertible) and [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md), the system uses only [`CustomAppIntentErrorConvertible`](customappintenterrorconvertible.md).

## Parameters

- `convertible`: The object to wrap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/init(wrapping:)-2lmed)*