# decodeErrorType()

**Framework**: Distributed  
**Kind**: method

Decode the specific error type that the distributed invocation target has recorded. Currently this effectively can only ever be `Error.self`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
final func decodeErrorType() throws -> (any Any.Type)?
```

#### Discussion

If the target known to not be throwing, or no error type was recorded, the method should return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationdecoder/decodeerrortype())*