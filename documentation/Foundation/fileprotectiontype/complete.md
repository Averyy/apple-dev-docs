# complete

**Framework**: Foundation  
**Kind**: property

The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let complete: FileProtectionType
```

## See Also

- [static let completeUnlessOpen: FileProtectionType](fileprotectiontype/completeunlessopen.md)
  The file is stored in an encrypted format on disk after it is closed.
- [static let completeUntilFirstUserAuthentication: FileProtectionType](fileprotectiontype/completeuntilfirstuserauthentication.md)
  The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.
- [static let none: FileProtectionType](fileprotectiontype/none.md)
  The file has no special protections associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileprotectiontype/complete)*