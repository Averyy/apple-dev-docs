# SecTrustedApplicationSetData(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the data of a given trusted app instance.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecTrustedApplicationSetData(_ appRef: SecTrustedApplication, _ data: CFData) -> OSStatus
```

```c
OSStatus SecTrustedApplicationSetData(SecTrustedApplicationRef appRef, CFDataRef data);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

If you use the [`SecTrustedApplicationCopyData(_:_:)`](./sectrustedapplicationcopydata%28_,_%29.md) method to extract the data from a trusted app instance for storage or transmission, you can use the [`SecTrustedApplicationSetData(_:_:)`](./sectrustedapplicationsetdata%28_,_%29.md) method to insert that data into a new trusted app. Doing so creates an object that identifies the same app as the original trusted app instance.

## Parameters

- `appRef`: A trusted application object.
- `data`: A reference to the data to set in the trusted application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustedapplicationsetdata(_:_:))*