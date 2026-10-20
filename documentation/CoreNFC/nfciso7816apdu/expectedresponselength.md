# expectedResponseLength

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The expected response data length (Le) in bytes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var expectedResponseLength: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger expectedResponseLength;
```

#### Discussion

Setting [`expectedResponseLength`](./expectedresponselength.md) with a value less than 0 means the Le field is absent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816apdu/expectedresponselength)*