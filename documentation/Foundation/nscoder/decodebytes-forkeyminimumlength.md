# decodeBytes(forKey:minimumLength:)

**Framework**: Foundation  
**Kind**: method

Decode bytes from the decoder for a given key. The length of the bytes must be greater than or equal to the `length` parameter. If the result exists, but is of insufficient length, then the decoder uses `failWithError` to fail the entire decode operation. The result of that is configurable on a per-NSCoder basis using `NSDecodingFailurePolicy`.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func decodeBytes(forKey key: String, minimumLength length: Int) -> UnsafePointer<UInt8>?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodebytes(forkey:minimumlength:))*