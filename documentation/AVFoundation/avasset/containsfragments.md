# containsFragments

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether at least one movie fragment extends the asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+

## Declaration

```swift
var containsFragments: Bool { get }
```

#### Discussion

For QuickTime movie files and MPEG-4 files, the value is [`true`](https://developer.apple.com/documentation/swift/true) if [`canContainFragments`](avasset/cancontainfragments.md) is [`true`](https://developer.apple.com/documentation/swift/true) and at least one `moof` box is present after the `moov` box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/containsfragments)*