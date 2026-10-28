# init(data:)

**Framework**: Core NFC  
**Kind**: init  
**Role**: Initializer

Creates an APDU object with the data buffer containing the full APDU.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init?(data: Data)
```

```objc
- (instancetype) initWithData:(NSData *) data;
```

## Return Value

A newly initialized APDU object.

## Parameters

- `data`: A data buffer containing the full APDU.

## See Also

### Creating an APDU Object
- [init(instructionClass: UInt8, instructionCode: UInt8, p1Parameter: UInt8, p2Parameter: UInt8, data: Data, expectedResponseLength: Int)](./init%28instructionclass,instructioncode,p1parameter,p2parameter,data,expectedresponselength%29.md)
  Creates an APDU object with the instruction class and code, parameter bytes, and expected response length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816apdu/init(data:))*