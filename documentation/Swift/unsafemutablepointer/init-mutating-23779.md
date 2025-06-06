# init(mutating:)

**Framework**: Swift  
**Kind**: init

Creates a mutable typed pointer referencing the same memory as the given immutable pointer.

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
init?(mutating other: UnsafePointer<Pointee>?)
```

## Parameters

- `other`: The immutable pointer to convert. If   is  ,   the result is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/init(mutating:)-23779)*