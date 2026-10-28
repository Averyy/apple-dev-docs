# isReady

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, readonly, getter=isReady) BOOL ready;
```

## Discussion

As soon as a reader session is successfully activated, radio-frequency discovery polling begins. When a tag is detected, [`readerSession:didDetectTags:`](../nfcreadersessiondelegate/readersession_diddetecttags_.md) is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol/isready)*