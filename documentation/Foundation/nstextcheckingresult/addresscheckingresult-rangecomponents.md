# addressCheckingResult(range:components:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a text checking result with the specified address components.

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
class func addressCheckingResult(range: NSRange, components: [NSTextCheckingKey : String]) -> NSTextCheckingResult
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](nstextcheckingresult/range.md) and a [`resultType`](nstextcheckingresult/resulttype.md) of [`address`](nstextcheckingresult/checkingtype/address.md).

## Parameters

- `range`: The range of the detected result.
- `components`: A dictionary containing the address components. The dictionary keys are described in  .

## See Also

- [var addressComponents: [NSTextCheckingKey : String]?](nstextcheckingresult/addresscomponents.md)
  The address dictionary of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/addresscheckingresult(range:components:))*