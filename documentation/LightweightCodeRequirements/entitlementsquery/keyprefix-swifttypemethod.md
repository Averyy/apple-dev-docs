# keyPrefix(_:)

**Framework**: LightweightCodeRequirements  
**Kind**: method

Match the specified key prefix at the root of the entitlements dicitonary. Chain additional qualifiers to constrain the value of the key.

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
static func keyPrefix(_ keyPrefix: String) -> EntitlementsQuery
```

#### Discussion

Keys are matched byte for byte (i.e. no unicode normalization occurs). keyPrefix will match only the first key with the prefix. Chained qualifiers will be applied to the value of that single key only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/entitlementsquery/keyprefix(_:)-swift.type.method)*