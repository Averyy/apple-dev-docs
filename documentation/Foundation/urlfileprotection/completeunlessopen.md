# completeUnlessOpen

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An option that instructs the system to store the file in an encrypted format on-disk after it closes.

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
static let completeUnlessOpen: URLFileProtection
```

```c
extern NSURLFileProtectionType const NSURLFileProtectionCompleteUnlessOpen;
```

## Discussion

Files with this type of protection can be created while the device is locked, but once closed, cannot be opened again until the device is unlocked. If the file is opened when unlocked, you may continue to access the file normally, even if the user locks the device. There is a small performance penalty when the file is created and opened, though not when being written to or read from. This can be mitigated by changing the file protection to [`complete`](./complete.md) when the device is unlocked.

## See Also

### Protection levels
- [static let complete: URLFileProtection](./complete.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.
- [static let completeUntilFirstUserAuthentication: URLFileProtection](./completeuntilfirstuserauthentication.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.
- [static let completeWhenUserInactive: URLFileProtection](./completewhenuserinactive.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.
- [static let none: URLFileProtection](./none.md)
  An option that indicates the file has no special protections associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlfileprotection/completeunlessopen)*