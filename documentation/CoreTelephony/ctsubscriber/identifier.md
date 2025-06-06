# identifier

**Framework**: Core Telephony  
**Kind**: property

An implementation-defined identifier used to correlate this subscriber with information vended by other APIs.

**Availability**:
- iOS 12.1+
- iPadOS 12.1+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

The format of the identifier can change across software releases. Therefore, do not persist this identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctsubscriber/identifier)*