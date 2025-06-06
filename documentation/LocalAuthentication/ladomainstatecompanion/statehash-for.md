# stateHash(for:)

**Framework**: Local Authentication  
**Kind**: method

Returns state hash data for the given companion type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func stateHash(for companionType: LACompanionType) -> Data?
```

#### Discussion

If database of paired devices of the given type was modified state hash data will change. Nature of such database changes cannot be determined but comparing data of state hash after different policy evaluation will reveal the fact database was changed between calls.

## Parameters

- `companionType`: The companion type for which state hash data should be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/ladomainstatecompanion/statehash(for:))*