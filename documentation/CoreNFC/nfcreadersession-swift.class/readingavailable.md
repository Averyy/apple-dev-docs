# readingAvailable

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

A Boolean value that determines whether the device supports NFC tag reading.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class var readingAvailable: Bool { get }
```

```objc
@property (class, nonatomic, readonly) BOOL readingAvailable;
```

#### Discussion

Before creating a reader session, always check the [`readingAvailable`](./readingavailable.md) property to determine whether the user’s device supports scanning for and detecting NFC tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class/readingavailable)*