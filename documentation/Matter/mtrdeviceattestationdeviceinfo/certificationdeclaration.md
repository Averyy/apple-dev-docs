# certificationDeclaration

**Framework**: Matter  
**Kind**: property

The certification declaration of the device, if available.  This is a DER-encoded string representing a CMS-formatted certification declaration.  May be nil only if attestation verification failed.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- tvOS 26.1+
- visionOS 26.1+
- watchOS 26.1+

## Declaration

```swift
var certificationDeclaration: Data? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdeviceattestationdeviceinfo/certificationdeclaration)*