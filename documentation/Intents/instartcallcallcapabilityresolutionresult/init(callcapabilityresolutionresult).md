# init(callCapabilityResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves the succesful start of a call with the specified capabilities.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(callCapabilityResolutionResult: INCallCapabilityResolutionResult)
```

```objc
- (instancetype) initWithCallCapabilityResolutionResult:(INCallCapabilityResolutionResult *) callCapabilityResolutionResult;
```

## Return Value

A new [`INStartCallCallCapabilityResolutionResult`](../instartcallcallcapabilityresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to start a call with the specified capabilities.

## Parameters

- `callCapabilityResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func unsupported(forReason: INStartCallCallCapabilityUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object specifying that resolution of the parameter wasn’t supported, for the specified reason.
- [enum INStartCallCallCapabilityUnsupportedReason](../instartcallcallcapabilityunsupportedreason.md)
  Constants indicating the reason the app can’t support starting the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcallcapabilityresolutionresult/init(callcapabilityresolutionresult:))*