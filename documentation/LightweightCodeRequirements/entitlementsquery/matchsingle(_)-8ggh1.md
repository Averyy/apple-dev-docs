# matchSingle(_:)

**Framework**: LightweightCodeRequirements  
**Kind**: method

Match the specified string against a string value (not an array).

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
func matchSingle(_ value: String) -> EntitlementsQuery
```

#### Discussion

Strings are matched byte for byte (i.e. no unicode normalization occurs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/entitlementsquery/matchsingle(_:)-8ggh1)*