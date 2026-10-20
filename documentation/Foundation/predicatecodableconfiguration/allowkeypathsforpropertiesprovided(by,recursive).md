# allowKeyPathsForPropertiesProvided(by:recursive:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
mutating func allowKeyPathsForPropertiesProvided<T>(by type: T.Type, recursive: Bool = false) where T : PredicateCodableKeyPathProviding
```

## See Also

### Allowing types and key paths
- [func allow(PredicateCodableConfiguration)](./allow%28_%29.md)
- [func allowPartialType(any Any.Type, identifier: String)](./allowpartialtype%28_,identifier%29.md)
- [func allowType(any Any.Type, identifier: String?)](./allowtype%28_,identifier%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicatecodableconfiguration/allowkeypathsforpropertiesprovided(by:recursive:))*