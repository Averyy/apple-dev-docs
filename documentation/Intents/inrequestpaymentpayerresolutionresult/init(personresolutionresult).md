# init(personResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a resolution result object with the specified person resolution result object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(personResolutionResult: INPersonResolutionResult)
```

```objc
- (instancetype) initWithPersonResolutionResult:(INPersonResolutionResult *) personResolutionResult;
```

## Return Value

An initialized resolution result object.

## Discussion

Typically, you do not call this method directly. Instead, you use the existing methods to create a resolution result of the appropriate type.

## Parameters

- `personResolutionResult`: The resolution result that resolves the payer information.

## See Also

### Creating a Resolution Result Object
- [class func unsupported(forReason: INRequestPaymentPayerUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that the specified value is not supported.
- [enum INRequestPaymentPayerUnsupportedReason](../inrequestpaymentpayerunsupportedreason.md)
  Constants indicating the reason for being unable to resolve the provider of the funds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentpayerresolutionresult/init(personresolutionresult:))*