# setNodeCredentials(_:password:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Sets credentials for the record’s node.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func setNodeCredentials(_ inUsername: String!, password inPassword: String!) throws
```

```objc
- (BOOL) setNodeCredentials:(NSString *) inUsername password:(NSString *) inPassword error:(NSError **) outError;
```

#### Discussion

If this function fails, the previous credentials for the node are used.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inUsername`: The username to use to authenticate with the node.
- `inPassword`: The password to use to authenticate with the node.

## See Also

### Managing Authentication
- [func changePassword(String!, toPassword: String!) throws](./changepassword%28_,topassword%29.md)
  Changes the record’s password.
- [func setNodeCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](./setnodecredentialswithrecordtype%28_,authenticationtype,authenticationitems,continueitems,context%29.md)
  Sets the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyExtended(withAuthenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](./verifyextended%28withauthenticationtype,authenticationitems,continueitems,context%29.md)
  Verifies the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyPassword(String!) throws](./verifypassword%28_%29.md)
  Verifies the password for interaction with the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/setnodecredentials(_:password:))*