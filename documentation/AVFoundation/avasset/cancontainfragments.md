# canContainFragments

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether you can extend the asset by fragments.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+

## Declaration

```swift
var canContainFragments: Bool { get }
```

#### Discussion

For QuickTime movie files and MPEG-4 files, the value is [`true`](https://developer.apple.com/documentation/swift/true) if an `mvex` box is present in the `moov` box. For those types, the `mvex` box signals the possible presence of later `moof` boxes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/cancontainfragments)*