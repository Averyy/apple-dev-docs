# decodeGenericSubstitutions()

**Framework**: Distributed  
**Kind**: method

Decode all generic substitutions that were recorded for this invocation.

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
final func decodeGenericSubstitutions() throws -> [any Any.Type]
```

#### Return Value

Array of all generic substitutions necessary to execute this invocation target.

#### Discussion

The values retrieved from here must be in the same order as they were recorded by [`recordGenericSubstitution(_:)`](distributedtargetinvocationencoder/recordgenericsubstitution(_:).md).

> **Note**: If decoding substitutions fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationdecoder/decodegenericsubstitutions())*