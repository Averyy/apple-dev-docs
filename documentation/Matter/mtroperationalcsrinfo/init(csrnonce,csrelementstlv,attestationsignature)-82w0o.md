# init(csrNonce:csrElementsTLV:attestationSignature:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init?(csrNonce: Data, csrElementsTLV: Data, attestationSignature: Data)
```

```objc
- (instancetype) initWithCSRNonce:(NSData *) csrNonce csrElementsTLV:(MTRTLVBytes) csrElementsTLV attestationSignature:(NSData *) attestationSignature;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtroperationalcsrinfo/init(csrnonce:csrelementstlv:attestationsignature:)-82w0o)*