# alignedDown(toMultipleOf:)

**Framework**: Swift  
**Kind**: method

Obtain the preceding pointer whose bit pattern is a multiple of `alignment`.

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
func alignedDown(toMultipleOf alignment: Int) -> UnsafeRawPointer
```

#### Return Value

A pointer aligned to `alignment`.

#### Discussion

If the bit pattern of `self` is a multiple of `alignment`, this function returns `self`.

## Parameters

- `alignment`: The alignment of the returned pointer, in bytes.    must be a whole power of 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawpointer/aligneddown(tomultipleof:))*