# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var code: INSearchForAccountsIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSearchForAccountsIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSearchForAccountsIntentResponseCode code;
```

#### Discussion

The value of this property is set automatically at initialization time and cannot be changed later.

## See Also

### Getting the Response Code
- [enum INSearchForAccountsIntentResponseCode](../insearchforaccountsintentresponsecode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponse/code)*