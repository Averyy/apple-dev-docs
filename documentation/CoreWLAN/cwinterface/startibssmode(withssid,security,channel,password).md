# startIBSSMode(withSSID:security:channel:password:)

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Creates a computer-to-computer (ad-hoc) network with the given network name, security type, and password on the specified channel.

**Availability**:
- macOS 10.7+ - Deprecated in 11.0

## Declaration

```swift
func startIBSSMode(withSSID ssidData: Data, security: CWIBSSModeSecurity, channel: Int, password: String?) throws
```

```objc
- (BOOL) startIBSSModeWithSSID:(NSData *) ssidData security:(CWIBSSModeSecurity) security channel:(NSUInteger) channel password:(NSString *) password error:(NSError **) error;
```

#### Discussion

If *name* is *nil*, the machine name will be used as the network name. This operation may require an administrator password.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `security`: The security type to be used.
- `channel`: The channel on which the network will be created.
- `password`: The password to be used. This paramter is not applicable to open system authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/startibssmode(withssid:security:channel:password:))*