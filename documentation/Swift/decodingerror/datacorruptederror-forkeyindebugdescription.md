# dataCorruptedError(forKey:in:debugDescription:)

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
static func dataCorruptedError<C>(forKey key: C.Key, in container: C, debugDescription: String) -> DecodingError where C : KeyedDecodingContainerProtocol
```

#### Return Value

A new `.dataCorrupted` error with the given information.

#### Discussion

The coding path for the returned error is constructed by appending the given key to the given container’s coding path.

- param key: The key which caused the failure.
- param container: The container in which the corrupted data was accessed.
- param debugDescription: A description of the error to aid in debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/decodingerror/datacorruptederror(forkey:in:debugdescription:))*