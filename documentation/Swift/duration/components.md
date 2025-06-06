# components

**Framework**: Swift  
**Kind**: property

The composite components of the `Duration`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var components: (seconds: Int64, attoseconds: Int64) { get }
```

#### Discussion

This is intended for facilitating conversions to existing time types. The attoseconds value will not exceed 1e18 or be lower than -1e18.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/components)*