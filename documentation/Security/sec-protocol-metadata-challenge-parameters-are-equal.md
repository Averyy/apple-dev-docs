# sec_protocol_metadata_challenge_parameters_are_equal(_:_:)

**Framework**: Security  
**Kind**: func

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func sec_protocol_metadata_challenge_parameters_are_equal(_ metadataA: sec_protocol_metadata_t, _ metadataB: sec_protocol_metadata_t) -> Bool
```

#### Return Value

Returns true if both metadata values have the same challenge parameters.

#### Discussion

```None
 Compare challenge-relevant information for two `sec_protocol_metadata` instances.

 This comparison includes all information relevant to a challenge request, including:
 distinguished names, signature algorithms, and supported certificate types.
 See Section 7.4.4 of RFC5246 for more details.
```

## Parameters

- `metadataA`: A   instance.
- `metadataB`: A   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_metadata_challenge_parameters_are_equal(_:_:))*