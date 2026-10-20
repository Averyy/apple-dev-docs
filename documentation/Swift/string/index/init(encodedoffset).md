# init(encodedOffset:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new index at the specified code unit offset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 4.2

> **Deprecated**: encodedOffset has been deprecated as most common usage is incorrect. Use String.Index(utf16Offset:in:) to achieve the same behavior.

## Declaration

```swift
init(encodedOffset offset: Int)
```

## Parameters

- `offset`: An offset in code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index/init(encodedoffset:))*