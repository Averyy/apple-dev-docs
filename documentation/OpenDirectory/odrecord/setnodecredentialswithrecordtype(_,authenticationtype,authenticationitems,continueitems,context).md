# setNodeCredentialsWithRecordType(_:authenticationType:authenticationItems:continueItems:context:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Sets the credentials for interaction with the record’s node using other types of authentication available to Open Directory.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func setNodeCredentialsWithRecordType(_ inRecordType: String!, authenticationType inType: String!, authenticationItems inItems: [Any]!, continueItems outItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context outContext: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws
```

```objc
- (BOOL) setNodeCredentialsWithRecordType:(ODRecordType) inRecordType authenticationType:(ODAuthenticationType) inType authenticationItems:(NSArray *) inItems continueItems:(NSArray **) outItems context:(id*) outContext error:(NSError **) outError;
```

## Discussion

If this function fails, the previous credentials for the node are used.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record type that uses the credentials. Can be `nil`. The default value is `kODRecordTypeUsers`.
- `inType`: The authentication type.
- `inItems`: An array of `NSString` or `NSData` objects to be used in the authentication process.
- `outItems`: An array of `NSData` objects returned from the authentication process, if any are returned; `nil` otherwise.
- `outContext`: The proper context if the authentication attempt requires a context; `nil` otherwise. If not `nil`, then more calls must be made with the Context to continue the authentication.

## See Also

### Managing Authentication
- [func changePassword(String!, toPassword: String!) throws](./changepassword%28_,topassword%29.md)
  Changes the record’s password.
- [func setNodeCredentials(String!, password: String!) throws](./setnodecredentials%28_,password%29.md)
  Sets credentials for the record’s node.
- [func verifyExtended(withAuthenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](./verifyextended%28withauthenticationtype,authenticationitems,continueitems,context%29.md)
  Verifies the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyPassword(String!) throws](./verifypassword%28_%29.md)
  Verifies the password for interaction with the record.
- [- passwordPolicyAndReturnError:](./passwordpolicyandreturnerror_.md)
  Returns a dictionary containing the password policy for the record.
- [- setNodeCredentialsUsingKerberosCache:error:](./setnodecredentialsusingkerberoscache_error_.md)
  Sets the credentials for interaction with the record’s node using a Kerberos cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/setnodecredentialswithrecordtype(_:authenticationtype:authenticationitems:continueitems:context:))*