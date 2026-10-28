# NSBinaryStoreSecureDecodingClasses

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

An additional set of classes to use while decoding a binary store.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let NSBinaryStoreSecureDecodingClasses: String
```

```c
extern NSString * const NSBinaryStoreSecureDecodingClasses;
```

## Discussion

This option is preferable to using [`NSBinaryStoreInsecureDecodingCompatibilityOption`](./nsbinarystoreinsecuredecodingcompatibilityoption.md).

## See Also

### Persistent Store Metadata Keys
- [let NSBinaryStoreInsecureDecodingCompatibilityOption: String](./nsbinarystoreinsecuredecodingcompatibilityoption.md)
  A flag that indicates Core Data decodes the binary store insecurely.
- [let NSPersistentStoreRemoteChangeNotificationPostOptionKey: String](./nspersistentstoreremotechangenotificationpostoptionkey.md)
  A key that indicates a persistent store posts a remote change notification for every write to the store, including writes by other processes.
- [let NSPersistentStoreModelVersionChecksumKey: String](./nspersistentstoremodelversionchecksumkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbinarystoresecuredecodingclasses)*