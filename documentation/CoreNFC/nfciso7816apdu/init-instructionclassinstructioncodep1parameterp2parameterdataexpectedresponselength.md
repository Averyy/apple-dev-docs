# init(instructionClass:instructionCode:p1Parameter:p2Parameter:data:expectedResponseLength:)

**Framework**: Core NFC  
**Kind**: init

Creates an APDU object with the instruction class and code, parameter bytes, and expected response length.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(instructionClass: UInt8, instructionCode: UInt8, p1Parameter: UInt8, p2Parameter: UInt8, data: Data, expectedResponseLength: Int)
```

#### Return Value

A newly initialized ISO 7816 APDU object.

#### Discussion

If your app needs more precise control of the APDU format, use [`init(data:)`](nfciso7816apdu/init(data:).md) to create the APDU object.

## Parameters

- `instructionClass`: The instruction class (CLA) byte value.
- `instructionCode`: The instruction code (INS) byte value.
- `p1Parameter`: The P1 parameter byte value.
- `p2Parameter`: The P2 parameter byte value.
- `data`: The data to transmit. The APDU object specifies the length of the transmission data in the Lc field.
- `expectedResponseLength`: The expected response data length (Le) in bytes. The value should be one of the following:

## See Also

- [init?(data: Data)](nfciso7816apdu/init(data:).md)
  Creates an APDU object with the data buffer containing the full APDU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816apdu/init(instructionclass:instructioncode:p1parameter:p2parameter:data:expectedresponselength:))*