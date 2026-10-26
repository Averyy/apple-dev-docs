# init(personResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves the succesful start of a call with the specified contact.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(personResolutionResult: INPersonResolutionResult)
```

```objc
- (instancetype) initWithPersonResolutionResult:(INPersonResolutionResult *) personResolutionResult;
```

#### Return Value

A new [`INStartCallContactResolutionResult`](../instartcallcontactresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to start a call with the specified capabilities.

## Parameters

- `personResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func unsupported(forReason: INStartCallContactUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object specifying that resolution of the parameter wasn’t supported, for the specified reason.
- [enum INStartCallContactUnsupportedReason](../instartcallcontactunsupportedreason.md)
  Constants indicating the reason the app can’t support starting a call with the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallcontactresolutionresult/init(personresolutionresult:))*