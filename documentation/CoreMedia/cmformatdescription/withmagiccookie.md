# withMagicCookie(_:)

**Framework**: Core Media  
**Kind**: method

Returns the magic cookie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func withMagicCookie<R>(_ body: (UnsafeRawBufferPointer?) throws -> R) rethrows -> R
```

## Parameters

- `body`: A pointer to the magic cookie in the audio format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/withmagiccookie(_:))*