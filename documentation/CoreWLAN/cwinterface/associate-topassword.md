# associate(to:password:)

**Framework**: Corewlan  
**Kind**: method

Associates to a given network using the given network passphrase.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func associate(to network: CWNetwork, password: String?) throws
```

#### Discussion

This method will block for the duration of the association. This operation may require an administrator password.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `network`: The network to which the interface will associate.
- `password`: The network passphrase or key. Required for association to WEP, WPA Personal, and WPA2 Personal networks.

## See Also

- [func associate(toEnterpriseNetwork: CWNetwork, identity: SecIdentity?, username: String?, password: String?) throws](cwinterface/associate(toenterprisenetwork:identity:username:password:).md)
  Connects to the given enterprise network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/associate(to:password:))*