# encode(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a JSON-encoded representation of the value you supply.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func encode<T>(_ value: T) throws -> Data where T : Encodable
```

## Return Value

The encoded JSON data.

## Discussion

If there’s a problem encoding the value you supply, this method throws an error based on the type of problem:

- The value fails to encode, or contains a nested value that fails to encode—this method throws the corresponding error.
- The value isn’t encodable as a JSON array or JSON object—this method throws the [`EncodingError.invalidValue(_:_:)`](../../Swift/encodingerror/invalidvalue%28_,_%29.md) error.
- The value contains an exceptional floating-point number (such as [`infinity`](../../Swift/floatingpoint/infinity.md) or [`nan`](../../Swift/floatingpoint/nan.md)) and you’re using the default [`JSONEncoder.NonConformingFloatEncodingStrategy`](./nonconformingfloatencodingstrategy-swift.enum.md) — this method throws the [`EncodingError.invalidValue(_:_:)`](../../Swift/encodingerror/invalidvalue%28_,_%29.md) error.

## Parameters

- `value`: The value to encode as JSON.

## See Also

### First Steps
- [init()](./init%28%29.md)
  Creates a new, reusable JSON encoder with the default formatting settings and encoding strategies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/encode(_:))*