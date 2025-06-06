# initialize(from:)

**Framework**: Swift  
**Kind**: method

Initializes memory starting at this pointer’s address with the elements of the given collection.

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
func initialize<C>(from source: C) where Pointee == C.Element, C : Collection
```

#### Discussion

The region of memory starting at this pointer and covering `source.count` instances of the pointer’s `Pointee` type must be uninitialized or `Pointee` must be a trivial type. After calling `initialize(from:)`, the region is initialized.

## Parameters

- `source`: A collection of elements of the pointer’s    type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/initialize(from:))*