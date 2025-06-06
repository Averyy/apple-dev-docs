# isAvailable

**Framework**: Core NFC  
**Kind**: property

A Boolean value that indicates whether a detected tag is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+

## Declaration

```swift
var isAvailable: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the tag is available in the current reader session. When a tag is removed from an RF field, it becomes unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctag-swift.enum/isavailable)*