# verifyPassword(_:)

**Framework**: Opendirectory  
**Kind**: method

Verifies the password for interaction with the record.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func verifyPassword(_ inPassword: String!) throws
```

#### Discussion

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inPassword`: The password for authenticating with the record.

## See Also

- [func changePassword(String!, toPassword: String!) throws](odrecord/changepassword(_:topassword:).md)
  Changes the record’s password.
- [func setNodeCredentials(String!, password: String!) throws](odrecord/setnodecredentials(_:password:).md)
  Sets credentials for the record’s node.
- [func setNodeCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](odrecord/setnodecredentialswithrecordtype(_:authenticationtype:authenticationitems:continueitems:context:).md)
  Sets the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyExtended(withAuthenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](odrecord/verifyextended(withauthenticationtype:authenticationitems:continueitems:context:).md)
  Verifies the credentials for interaction with the record’s node using other types of authentication available to Open Directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/verifypassword(_:))*