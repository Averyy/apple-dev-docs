# associate(toEnterpriseNetwork:identity:username:password:)

**Framework**: Core WLAN  
**Kind**: method

Connects to the given enterprise network.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func associate(toEnterpriseNetwork network: CWNetwork, identity: SecIdentity?, username: String?, password: String?) throws
```

#### Discussion

This method will block for the duration of the association. This operation may require an administrator password.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `network`: The network to which the interface will associate.
- `identity`: The identity to use for IEEE 802.1X authentication. Holds the corresponding client certificate.
- `username`: The username to use for IEEE 802.1X authentication.
- `password`: The password to use for IEEE 802.1X authentication.

## See Also

- [func associate(to: CWNetwork, password: String?) throws](cwinterface/associate(to:password:).md)
  Associates to a given network using the given network passphrase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/associate(toenterprisenetwork:identity:username:password:))*