# init(from:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a progress instance by decoding from the given decoder.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder`: The decoder to read data from.

## See Also

### Encoding and decoding a session’s progress
- [func encode(to: any Encoder) throws](./encode%28to%29.md)
  Encodes the progress value into the given encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlprogress/init(from:))*