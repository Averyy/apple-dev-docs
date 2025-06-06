# setCredentialsUsingKerberosCache(_:)

**Framework**: Open Directory  
**Kind**: method

Sets the credentials for interaction with the node using a Kerberos cache.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func setCredentialsUsingKerberosCache(_ inCacheName: String!) throws
```

#### Discussion

If this function fails, the previous credentials for the node are used.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inCacheName`: The name of the Kerberos cache.

## See Also

- [func setCredentialsWithRecordType(String!, recordName: String!, password: String!) throws](odnode/setcredentialswithrecordtype(_:recordname:password:).md)
  Sets credentials for interacting with the node.
- [func setCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](odnode/setcredentialswithrecordtype(_:authenticationtype:authenticationitems:continueitems:context:).md)
  Sets the credentials for interaction with the node using other types of authentication available to Open Directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/setcredentialsusingkerberoscache(_:))*