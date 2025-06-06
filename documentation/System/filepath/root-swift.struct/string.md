# string

**Framework**: System  
**Kind**: property

On Unix, this returns `"/"`.

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

On Windows, interprets the root’s content as UTF-16 on Windows.

This property is equivalent to calling `String(decoding: root)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/root-swift.struct/string)*