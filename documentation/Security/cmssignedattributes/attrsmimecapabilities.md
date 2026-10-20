# attrSmimeCapabilities

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

Identify signature, encryption, and digest algorithms supported by the encoder.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var attrSmimeCapabilities: CMSSignedAttributes { get }
```

```c
kCMSAttrSmimeCapabilities
```

#### Discussion

Using this attribute doesn’t change the encoding. See [RFC 2311: S/MIME Version 2 Message Specification](https://tools.ietf.org/html/rfc2311) section 2.5.2 for more information about the capabilities attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmssignedattributes/attrsmimecapabilities)*