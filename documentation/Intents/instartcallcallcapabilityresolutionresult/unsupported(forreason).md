# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object specifying that resolution of the parameter wasn’t supported, for the specified reason.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func unsupported(forReason reason: INStartCallCallCapabilityUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INStartCallCallCapabilityUnsupportedReason) reason;
```

#### Return Value

A new [`INStartCallCallCapabilityResolutionResult`](../instartcallcallcapabilityresolutionresult.md) object.

#### Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The call capability that isn’t supported.

## See Also

### Creating a Resolution Result Object
- [init(callCapabilityResolutionResult: INCallCapabilityResolutionResult)](./init%28callcapabilityresolutionresult%29.md)
  Creates an object whose resolution involves the succesful start of a call with the specified capabilities.
- [enum INStartCallCallCapabilityUnsupportedReason](../instartcallcallcapabilityunsupportedreason.md)
  Constants indicating the reason the app can’t support starting the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcallcapabilityresolutionresult/unsupported(forreason:))*