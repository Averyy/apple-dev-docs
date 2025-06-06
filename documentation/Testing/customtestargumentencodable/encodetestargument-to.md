# encodeTestArgument(to:)

**Framework**: Swift Testing  
**Kind**: method  
**Required**: Yes

Encode this test argument.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
func encodeTestArgument(to encoder: some Encoder) throws
```

#### Discussion

> **Note**: Any error encountered during encoding.

Any error encountered during encoding.

The encoded form of a test argument should be stable and unique to allow re-running specific test cases of a parameterized test function. For optimal performance, large values which are not necessary to uniquely identify the test argument later should be omitted. Encoded values do not need to be human-readable.

For more information on how to implement this function, see the documentation for [`Encodable`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/encodable).

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/customtestargumentencodable/encodetestargument(to:))*