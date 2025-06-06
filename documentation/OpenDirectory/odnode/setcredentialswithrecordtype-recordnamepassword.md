# setCredentialsWithRecordType(_:recordName:password:)

**Framework**: Opendirectory  
**Kind**: method

Sets credentials for interacting with the node.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!) throws
```

#### Discussion

If this function fails, the previous credentials for the node are used.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record type that uses the credentials. Can be  . The default value is  .
- `inRecordName`: The username to use to authenticate with the node.
- `inPassword`: The password to use to authenticate with the node.

## See Also

- [func setCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](odnode/setcredentialswithrecordtype(_:authenticationtype:authenticationitems:continueitems:context:).md)
  Sets the credentials for interaction with the node using other types of authentication available to Open Directory.
- [func setCredentialsUsingKerberosCache(String!) throws](odnode/setcredentialsusingkerberoscache(_:).md)
  Sets the credentials for interaction with the node using a Kerberos cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/setcredentialswithrecordtype(_:recordname:password:))*