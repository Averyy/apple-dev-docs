# NSDecimalString(_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a string representation of the decimal value appropriate for the specified locale.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSDecimalString(_ dcm: UnsafePointer<Decimal>, _ locale: Any?) -> String
```

## Parameters

- `dcm`: The decimal value to represent.
- `locale`: Either an instance of   or a dictionary with a string value corresponding to the   key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalstring(_:_:))*