# accounts

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The accounts found during the search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var accounts: [INPaymentAccount]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INPaymentAccount *> * accounts;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INPaymentAccount *> * accounts;
```

#### Discussion

Use this property to specify the search results. Each INPaymentAccount object should contain information about the account, including the current balance if the user requested that information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponse/accounts)*