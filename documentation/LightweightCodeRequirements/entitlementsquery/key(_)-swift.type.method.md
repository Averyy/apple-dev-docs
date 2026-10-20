# key(_:)

**Framework**: LightweightCodeRequirements  
**Kind**: method

Match against the specified key name at the root of the entitlements dictionary.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static func key(_ keyName: String) -> EntitlementsQuery
```

#### Discussion

Keys are matched byte for byte (i.e. no unicode normalization occurs). Chain additional qualifiers to constrain the value of the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/entitlementsquery/key(_:)-swift.type.method)*