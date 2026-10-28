# isAvailable

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a detected tag is available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Declaration

```swift
var isAvailable: Bool { get }
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the tag is available in the current reader session. When a tag is removed from an RF field, it becomes unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctag-swift.enum/isavailable)*