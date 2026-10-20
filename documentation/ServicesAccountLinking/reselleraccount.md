# ResellerAccount

**Framework**: ServicesAccountLinking  
**Kind**: struct  
**Role**: Structure

Reseller account type for linking with Apple Media & Purchases accounts.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
struct ResellerAccount
```

```c
typedef struct { ... } SALResellerAccount;
```

## Topics

### Registration methods
- [static func registerToken(String) async throws](./reselleraccount/registertoken%28_%29.md)
  Registers a signed token with the user’s Media & Purchases account.
- [static func registerIdentifier(String) async throws](./reselleraccount/registeridentifier%28_%29.md)
  Registers an account identifier with the user’s Media & Purchases account.
### Initializers
- [init()](./reselleraccount/init%28%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount)*