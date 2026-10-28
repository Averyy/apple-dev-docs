# load(fromByteOffset:as:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a value constructed from the raw memory at the specified offset.

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
func load<T>(fromByteOffset offset: Int, as type: T.Type) -> T where T : ConvertibleFromBytes
```

## Return Value

A new value of type `T`, read from `offset`.

## Discussion

The range of bytes required to construct a value of type `T` starting at `offset` must be completely within the span. `offset` is not required to be aligned for `T`.

## Parameters

- `offset`: The offset from the beginning of this span, in bytes. `offset` must be nonnegative.
- `type`: The type of the instance to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/load(frombyteoffset:as:))*