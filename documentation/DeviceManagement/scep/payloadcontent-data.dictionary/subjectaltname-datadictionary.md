# SCEP.PayloadContent.SubjectAltName

**Framework**: Device Management  
**Kind**: dictionary

An optional dictionary that provides values required by the CA for issuing a certificate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SCEP.PayloadContent.SubjectAltName
```

#### Discussion

You can specify a single string or an array of strings for each key. The values you specify depend on the CA you’re using but might include DNS name, URL, or email values. For an example, see the [`Example SCEP Configuration Profile`](configuring-multiple-devices-using-profiles#Example-SCEP-Configuration-Profile.md) or [`Over-the-Air Profile Delivery and Configuration`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009505).

## See Also

- [object SCEP.PayloadContent](scep/payloadcontent-data.dictionary.md)
  The SCEP dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scep/payloadcontent-data.dictionary/subjectaltname-data.dictionary)*