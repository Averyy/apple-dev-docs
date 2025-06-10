# none

**Framework**: Foundation  
**Kind**: property

The file has no special protections associated with it.

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
static let none: FileProtectionType
```

#### Discussion

A file with this type of protection can be read from or written to at any time.

## See Also

- [static let complete: FileProtectionType](fileprotectiontype/complete.md)
  The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.
- [static let completeUnlessOpen: FileProtectionType](fileprotectiontype/completeunlessopen.md)
  The file is stored in an encrypted format on disk after it is closed.
- [static let completeUntilFirstUserAuthentication: FileProtectionType](fileprotectiontype/completeuntilfirstuserauthentication.md)
  The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileprotectiontype/none)*