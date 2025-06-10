# completeWhenUserInactive

**Framework**: Foundation  
**Kind**: property

An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let completeWhenUserInactive: URLFileProtection
```

#### Discussion

After the first unlock, your app can access the file and continue to access it even if the person using it subsequently locks the device. After access expires, your app can’t access the file until the person using the device unlocks it again.

## See Also

- [static let complete: URLFileProtection](urlfileprotection/complete.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.
- [static let completeUnlessOpen: URLFileProtection](urlfileprotection/completeunlessopen.md)
  An option that instructs the system to store the file in an encrypted format on-disk after it closes.
- [static let completeUntilFirstUserAuthentication: URLFileProtection](urlfileprotection/completeuntilfirstuserauthentication.md)
  An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.
- [static let none: URLFileProtection](urlfileprotection/none.md)
  An option that indicates the file has no special protections associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlfileprotection/completewhenuserinactive)*