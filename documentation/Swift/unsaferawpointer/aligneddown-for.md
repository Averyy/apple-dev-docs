# alignedDown(for:)

**Framework**: Swift  
**Kind**: method

Obtain the preceding pointer properly aligned to store a value of type `T`.

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
func alignedDown<T>(for type: T.Type) -> UnsafeRawPointer where T : ~Copyable
```

#### Return Value

A pointer properly aligned to store a value of type `T`.

#### Discussion

If `self` is properly aligned for accessing `T`, this function returns `self`.

## Parameters

- `type`: The type to be stored at the returned address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawpointer/aligneddown(for:))*