# recordGenericSubstitution(_:)

**Framework**: Distributed  
**Kind**: method  
**Required**: Yes

The arguments must be encoded order-preserving, and once `decodeGenericSubstitutions` is called, the substitutions must be returned in the same order in which they were recorded.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
mutating func recordGenericSubstitution<T>(_ type: T.Type) throws
```

## Parameters

- `type`: A generic substitution type to be recorded for this invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/recordgenericsubstitution(_:))*