# SecCertificateCopyValues(_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a dictionary that represents a certificate’s contents.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecCertificateCopyValues(_ certificate: SecCertificate, _ keys: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?
```

## Mentions

- [Getting Certificate Values](getting-certificate-values.md)

#### Return Value

A dictionary containing the specified values from the certificate or `NULL` if an error occurs. In Objective-C, free this dictionary with a call to the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function when you are done with it.

#### Discussion

Each entry in this dictionary is itself a dictionary with the keys described in [`Certificate Property Keys`](certificate-property-keys.md).

## Parameters

- `certificate`: The certificate from which values should be copied.
- `keys`: Only OIDs that represent top-level keys in the returned dictionary can be specified. Unknown OIDs are ignored. See   for the list of known OIDs.
- `error`: A pointer to a  doc://com.apple.documentation/documentation/corefoundation/cferror-ru8  variable where an error object is stored upon failure. If not  , the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopyvalues(_:_:_:))*