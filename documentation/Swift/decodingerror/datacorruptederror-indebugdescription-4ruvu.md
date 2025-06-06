# dataCorruptedError(in:debugDescription:)

**Framework**: Swift  
**Kind**: method

Returns a new `.dataCorrupted` error using a constructed coding path and the given debug description.

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
static func dataCorruptedError(in container: any SingleValueDecodingContainer, debugDescription: String) -> DecodingError
```

#### Return Value

A new `.dataCorrupted` error with the given information.

#### Discussion

The coding path for the returned error is the given container’s coding path.

- param container: The container in which the corrupted data was accessed.
- param debugDescription: A description of the error to aid in debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decodingerror/datacorruptederror(in:debugdescription:)-4ruvu)*