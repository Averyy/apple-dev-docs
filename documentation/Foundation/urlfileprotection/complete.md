# complete

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let complete: URLFileProtection
```

```c
extern NSURLFileProtectionType const NSURLFileProtectionComplete;
```

## See Also

### Protection levels
- [static let completeUnlessOpen: URLFileProtection](./completeunlessopen.md)
  An option that instructs the system to store the file in an encrypted format on-disk after it closes.
- [static let completeUntilFirstUserAuthentication: URLFileProtection](./completeuntilfirstuserauthentication.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.
- [static let completeWhenUserInactive: URLFileProtection](./completewhenuserinactive.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.
- [static let none: URLFileProtection](./none.md)
  An option that indicates the file has no special protections associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlfileprotection/complete)*