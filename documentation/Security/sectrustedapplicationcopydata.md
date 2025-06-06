# SecTrustedApplicationCopyData(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the data of a trusted app instance.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func SecTrustedApplicationCopyData(_ appRef: SecTrustedApplication, _ data: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The trusted app instance created by the [`SecTrustedApplicationCreateFromPath(_:_:)`](sectrustedapplicationcreatefrompath(_:_:).md) method includes data that uniquely identifies the app, such as a cryptographic hash of the app. The operating system uses this data to verify that the app is unaltered since the trusted app instance was created. When an app requests access to an item in the keychain for which it is designated as a trusted app, the operating system checks this data before granting access.

Use the [`SecTrustedApplicationCopyData(_:_:)`](sectrustedapplicationcopydata(_:_:).md) function to extract this data from the trusted app instance for storage or for transmission over the network. Use the [`SecTrustedApplicationSetData(_:_:)`](sectrustedapplicationsetdata(_:_:).md) function to insert that data back into a trusted app instance. Note that this data is opaque: there’s no way to interpret it.

## Parameters

- `appRef`: A trusted app from which to retrieve data. Use the   method to create a trusted app instance.
- `data`: On return, points to an opaque data instance. Call the   method to release the data when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustedapplicationcopydata(_:_:))*