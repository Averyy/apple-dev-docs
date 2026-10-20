# disallowKeyPathsForPropertiesProvided(by:recursive:)

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
mutating func disallowKeyPathsForPropertiesProvided<T>(by type: T.Type, recursive: Bool = false) where T : PredicateCodableKeyPathProviding
```

## See Also

### Disallowing types and key paths
- [func disallowPartialType(any Any.Type)](./disallowpartialtype%28_%29.md)
- [func disallowType(any Any.Type)](./disallowtype%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicatecodableconfiguration/disallowkeypathsforpropertiesprovided(by:recursive:))*