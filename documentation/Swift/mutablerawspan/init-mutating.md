# init(mutating:)

**Framework**: Swift  
**Kind**: init

Mutate the elements of a typed span as bytes.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
init<Element>(mutating elements: inout MutableSpan<Element>) where Element : ConvertibleFromBytes, Element : ConvertibleToBytes
```

#### Discussion

The stride of `Element` must equal its size, and the starting address of `elements` must be well-aligned for `Element`.

## Parameters

- `elements`: A typed span to reinterpret as raw bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/init(mutating:))*