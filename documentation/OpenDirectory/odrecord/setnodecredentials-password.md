# setNodeCredentials(_:password:)

**Framework**: Opendirectory  
**Kind**: method

Sets credentials for the record’s node.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func setNodeCredentials(_ inUsername: String!, password inPassword: String!) throws
```

#### Discussion

If this function fails, the previous credentials for the node are used.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inUsername`: The username to use to authenticate with the node.
- `inPassword`: The password to use to authenticate with the node.

## See Also

- [func changePassword(String!, toPassword: String!) throws](odrecord/changepassword(_:topassword:).md)
  Changes the record’s password.
- [func setNodeCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](odrecord/setnodecredentialswithrecordtype(_:authenticationtype:authenticationitems:continueitems:context:).md)
  Sets the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyExtended(withAuthenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](odrecord/verifyextended(withauthenticationtype:authenticationitems:continueitems:context:).md)
  Verifies the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyPassword(String!) throws](odrecord/verifypassword(_:).md)
  Verifies the password for interaction with the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/setnodecredentials(_:password:))*