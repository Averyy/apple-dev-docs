# constantData(at:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a pointer to an inline, constant-data argument within the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func constantData(at index: Int) -> UnsafeMutableRawPointer
```

#### Return Value

A pointer to the location in the buffer to which you should write the constant data.

#### Discussion

Constants declared contiguously in the Metal shading language (in an array or structure) are contiguous in memory. You can encode contiguous ranges of inlined constant data through a pointer to the first constant.

To encode inlined constant data into the argument buffer, perform a memory copy operation from your data’s source pointer to the returned destination pointer.

## Parameters

- `index`: The index of an inline, constant-data argument within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/constantdata(at:))*