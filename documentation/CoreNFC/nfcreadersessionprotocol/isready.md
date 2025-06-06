# isReady

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the reader session is started and ready to use.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isReady: Bool { get }
```

#### Discussion

As soon as a reader session is successfully activated, radio-frequency discovery polling begins. When a tag is detected, [`readerSession:didDetectTags:`](nfcreadersessiondelegate/readersession:diddetecttags:.md) is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol/isready)*