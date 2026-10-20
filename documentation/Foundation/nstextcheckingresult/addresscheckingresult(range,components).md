# addressCheckingResult(range:components:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSTextCheckingResult *) addressCheckingResultWithRange:(NSRange) range components:(NSDictionary<NSString *,NSString *> *) components;
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](./range.md) and a [`resultType`](./resulttype.md) of [`address`](./checkingtype/address.md).

## Parameters

- `range`: The range of the detected result.
- `components`: A dictionary containing the address components. The dictionary keys are described in [Keys for Address Components](../keys-for-address-components.md).

## See Also

### Text Checking Results for Addresses
- [var addressComponents: [NSTextCheckingKey : String]?](./addresscomponents.md)
  The address dictionary of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/addresscheckingresult(range:components:))*