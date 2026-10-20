# init(wrapping:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an error from a custom app intent convertible value.

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
init(wrapping convertible: some CustomAppIntentErrorConvertible)
```

#### Discussion

The system calls this initializer for errors thrown from [`perform()`](../appintent/perform%28%29.md) that conform to [`CustomAppIntentErrorConvertible`](../customappintenterrorconvertible.md).

If the error conforms to both [`CustomLocalizedStringResourceConvertible`](../../Foundation/customlocalizedstringresourceconvertible.md) and [`CustomAppIntentErrorConvertible`](../customappintenterrorconvertible.md), the system uses only [`CustomAppIntentErrorConvertible`](../customappintenterrorconvertible.md).

## Parameters

- `convertible`: The object to wrap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/init(wrapping:)-2lmed)*