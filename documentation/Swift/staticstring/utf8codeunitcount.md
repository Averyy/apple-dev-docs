# utf8CodeUnitCount

**Framework**: Swift  
**Kind**: property

The number of UTF-8 code units (excluding the null terminator).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var utf8CodeUnitCount: Int { get }
```

#### Discussion

> ❗ **Important**: Accessing this property when `hasPointerRepresentation` is `false` triggers a runtime error.

Accessing this property when `hasPointerRepresentation` is `false` triggers a runtime error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/staticstring/utf8codeunitcount)*