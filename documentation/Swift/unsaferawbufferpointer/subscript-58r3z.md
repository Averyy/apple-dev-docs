# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the bytes in the specified memory region.

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
subscript(bounds: Range<Int>) -> UnsafeRawBufferPointer.SubSequence { get }
```

## Parameters

- `bounds`: The range of byte offsets to access. The upper and   lower bounds of the range must be in the range  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawbufferpointer/subscript(_:)-58r3z)*