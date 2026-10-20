# publicKey(fromCSR:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
class func publicKey(fromCSR csr: Data) throws -> Data
```

```objc
+ (NSData *) publicKeyFromCSR:(MTRCSRDERBytes) csr error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificates/publickey(fromcsr:))*