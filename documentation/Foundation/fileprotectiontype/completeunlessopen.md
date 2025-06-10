# completeUnlessOpen

**Framework**: Foundation  
**Kind**: property

The file is stored in an encrypted format on disk after it is closed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let completeUnlessOpen: FileProtectionType
```

#### Discussion

Files with this type of protection can be created while the device is locked, but once closed, cannot be opened again until the device is unlocked. If the file is opened when unlocked, you may continue to access the file normally, even if the user locks the device. There is a small performance penalty when the file is created and opened, though not when being written to or read from. This can be mitigated by changing the file protection to [`complete`](fileprotectiontype/complete.md) when the device is unlocked.

## See Also

- [static let complete: FileProtectionType](fileprotectiontype/complete.md)
  The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.
- [static let completeUntilFirstUserAuthentication: FileProtectionType](fileprotectiontype/completeuntilfirstuserauthentication.md)
  The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.
- [static let none: FileProtectionType](fileprotectiontype/none.md)
  The file has no special protections associated with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileprotectiontype/completeunlessopen)*