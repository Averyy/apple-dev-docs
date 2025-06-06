# setCredentialsWithRecordType(_:authenticationType:authenticationItems:continueItems:context:)

**Framework**: Open Directory  
**Kind**: method

Sets the credentials for interaction with the node using other types of authentication available to Open Directory.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func setCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws
```

#### Discussion

If this function fails, the previous credentials for the node are used.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record type that uses the credentials. Can be  . The default value is  .
- `inType`: The authentication type.
- `inItems`: An array of   or   objects to be used in the authentication process.
- `outItems`: An array of   objects returned from the authentication process, if any are returned;   otherwise.
- `outContext`: The proper context if the authentication attempt requires a context;   otherwise. If not  , then more calls must be made with the Context to continue the authentication.

## See Also

- [func setCredentialsWithRecordType(String!, recordName: String!, password: String!) throws](odnode/setcredentialswithrecordtype(_:recordname:password:).md)
  Sets credentials for interacting with the node.
- [func setCredentialsUsingKerberosCache(String!) throws](odnode/setcredentialsusingkerberoscache(_:).md)
  Sets the credentials for interaction with the node using a Kerberos cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/setcredentialswithrecordtype(_:authenticationtype:authenticationitems:continueitems:context:))*