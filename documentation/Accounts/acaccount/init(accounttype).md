# init(accountType:)

**Framework**: Accounts  
**Kind**: init  
**Role**: Initializer

Initializes a new account of the specified type.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
init!(accountType type: ACAccountType!)
```

```objc
- (instancetype) initWithAccountType:(ACAccountType *) type;
```

## Return Value

The newly initialized account.

## Parameters

- `type`: The type of this account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccount/init(accounttype:))*