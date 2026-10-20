# resultData

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The returned data without SW1-SW2 bytes, if any.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var resultData: Data? { get set }
```

```objc
@property (nullable) NSData * resultData;
```

## See Also

### Accessing Response Data
- [var resultSW: UInt16](./resultsw.md)
  The SW1-SW2 status bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/resultdata)*