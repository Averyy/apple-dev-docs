# associate(to:password:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Associates to a given network using the given network passphrase.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func associate(to network: CWNetwork, password: String?) throws
```

```objc
- (BOOL) associateToNetwork:(CWNetwork *) network password:(NSString *) password error:(NSError **) error;
```

## Discussion

This method will block for the duration of the association. This operation may require an administrator password.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `network`: The network to which the interface will associate.
- `password`: The network passphrase or key. Required for association to WEP, WPA Personal, and WPA2 Personal networks.

## See Also

### Associating to a network
- [func associate(toEnterpriseNetwork: CWNetwork, identity: SecIdentity?, username: String?, password: String?) throws](./associate%28toenterprisenetwork,identity,username,password%29.md)
  Connects to the given enterprise network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/associate(to:password:))*