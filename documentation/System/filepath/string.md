# string

**Framework**: System  
**Kind**: property

Creates a string by interpreting the path’s content as UTF-8 on Unix and UTF-16 on Windows.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var string: String { get }
```

#### Discussion

This property is equivalent to calling `String(decoding: path)`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/string)*