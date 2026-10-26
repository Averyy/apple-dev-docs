# setNodeCredentialsUsingKerberosCache:error:

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Sets the credentials for interaction with the record’s node using a Kerberos cache.

**Availability**:
- Mac Catalyst
- macOS 10.6+ - Deprecated in 10.7

## Declaration

```objc
- (BOOL) setNodeCredentialsUsingKerberosCache:(NSString *) inCacheName error:(NSError **) outError;
```

#### Return Value

[`true`](../../Swift/true.md) if the credentials are successfully set; otherwise, [`false`](../../Swift/false.md).

#### Discussion

If this function fails, the previous credentials for the node are used.

## Parameters

- `inCacheName`: The name of the Kerberos cache.
- `outError`: An error reference for error details. Can be `nil`.

## See Also

### Managing Authentication
- [func changePassword(String!, toPassword: String!) throws](./changepassword%28_,topassword%29.md)
  Changes the record’s password.
- [- passwordPolicyAndReturnError:](./passwordpolicyandreturnerror_.md)
  Returns a dictionary containing the password policy for the record.
- [func setNodeCredentials(String!, password: String!) throws](./setnodecredentials%28_,password%29.md)
  Sets credentials for the record’s node.
- [func setNodeCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](./setnodecredentialswithrecordtype%28_,authenticationtype,authenticationitems,continueitems,context%29.md)
  Sets the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyExtended(withAuthenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](./verifyextended%28withauthenticationtype,authenticationitems,continueitems,context%29.md)
  Verifies the credentials for interaction with the record’s node using other types of authentication available to Open Directory.
- [func verifyPassword(String!) throws](./verifypassword%28_%29.md)
  Verifies the password for interaction with the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/setnodecredentialsusingkerberoscache:error:)*