# setCredentialsWithRecordType(_:recordName:password:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Sets credentials for interacting with the node.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func setCredentialsWithRecordType(_ inRecordType: String!, recordName inRecordName: String!, password inPassword: String!) throws
```

```objc
- (BOOL) setCredentialsWithRecordType:(ODRecordType) inRecordType recordName:(NSString *) inRecordName password:(NSString *) inPassword error:(NSError **) outError;
```

#### Discussion

If this function fails, the previous credentials for the node are used.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record type that uses the credentials. Can be `nil`. The default value is `kODRecordTypeUsers`.
- `inRecordName`: The username to use to authenticate with the node.
- `inPassword`: The password to use to authenticate with the node.

## See Also

### Setting Node Credentials
- [func setCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](./setcredentialswithrecordtype%28_,authenticationtype,authenticationitems,continueitems,context%29.md)
  Sets the credentials for interaction with the node using other types of authentication available to Open Directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/setcredentialswithrecordtype(_:recordname:password:))*