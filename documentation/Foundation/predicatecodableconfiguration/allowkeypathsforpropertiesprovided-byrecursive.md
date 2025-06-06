# allowKeyPathsForPropertiesProvided(by:recursive:)

**Framework**: Foundation  
**Kind**: method

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

- [func allow(PredicateCodableConfiguration)](predicatecodableconfiguration/allow(_:).md)
- [func allowPartialType(any Any.Type, identifier: String)](predicatecodableconfiguration/allowpartialtype(_:identifier:).md)
- [func allowType(any Any.Type, identifier: String?)](predicatecodableconfiguration/allowtype(_:identifier:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicatecodableconfiguration/allowkeypathsforpropertiesprovided(by:recursive:))*