# NSHTTPPropertyStatusReasonKey

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Key for the remainder of the HTTP status line following the status code, returned as an `NSString` object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```c
extern NSString * const NSHTTPPropertyStatusReasonKey;
```

## Discussion

This string usually contains an explanation of the error in English. Because this string is taken straight from the server response, it’s not localized.

## See Also

### Resource Property Keys
- [NSFTPPropertyActiveTransferModeKey](./nsftppropertyactivetransfermodekey.md)
  Key for retrieving whether in active transfer mode, returned as a boolean wrapped in an `NSNumber` object.
- [NSFTPPropertyFTPProxy](./nsftppropertyftpproxy.md)
  `NSDictionary` containing proxy information to use in place of proxy identified in `SystemConfiguration.framework`.
- [NSFTPPropertyFileOffsetKey](./nsftppropertyfileoffsetkey.md)
  Key for retrieving the file offset, returned as an `NSNumber` object. The default value for this key is zero.
- [NSFTPPropertyUserLoginKey](./nsftppropertyuserloginkey.md)
  Key for the user login, returned as an `NSString` object.
- [NSFTPPropertyUserPasswordKey](./nsftppropertyuserpasswordkey.md)
  Key for the user password, returned as an `NSString` object.
- [NSHTTPPropertyErrorPageDataKey](./nshttppropertyerrorpagedatakey.md)
  Key for retrieving an error page as an `NSData` object.
- [NSHTTPPropertyHTTPProxy](./nshttppropertyhttpproxy.md)
  Key for retrieving the `NSDictionary` object containing proxy information to use in place of proxy identified in `SystemConfiguration.framework`.
- [NSHTTPPropertyRedirectionHeadersKey](./nshttppropertyredirectionheaderskey.md)
  Key for retrieving the redirection headers as an `NSDictionary` object with each header value keyed to the header name.
- [NSHTTPPropertyServerHTTPVersionKey](./nshttppropertyserverhttpversionkey.md)
  Key for retrieving the HTTP version as an `NSString` object containing the initial server status line up to the first space.
- [NSHTTPPropertyStatusCodeKey](./nshttppropertystatuscodekey.md)
  Key for the status code, returned as an integer wrapped in an `NSNumber` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshttppropertystatusreasonkey)*