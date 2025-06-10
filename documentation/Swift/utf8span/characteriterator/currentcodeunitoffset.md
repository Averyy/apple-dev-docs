# currentCodeUnitOffset

**Framework**: Swift  
**Kind**: property

The byte offset of the start of the next `Character`. This is always scalar-aligned. It is always `Character`-aligned relative to the last call to `reset` (or the start of the span if not called).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var currentCodeUnitOffset: Int { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/currentcodeunitoffset)*