# phoneNumberCheckingResult(range:phoneNumber:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a text checking result with the specified phone number.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func phoneNumberCheckingResult(range: NSRange, phoneNumber: String) -> NSTextCheckingResult
```

```objc
+ (NSTextCheckingResult *) phoneNumberCheckingResultWithRange:(NSRange) range phoneNumber:(NSString *) phoneNumber;
```

## Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](./range.md) and a [`resultType`](./resulttype.md) of [`phoneNumber`](./checkingtype/phonenumber.md).

## Parameters

- `range`: The range of the detected result.
- `phoneNumber`: The phone number.

## See Also

### Text Checking Results for Phone Numbers
- [var phoneNumber: String?](./phonenumber.md)
  The phone number of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/phonenumbercheckingresult(range:phonenumber:))*