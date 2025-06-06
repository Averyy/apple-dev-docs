# decodeReturnType()

**Framework**: Distributed  
**Kind**: method

Attempt to decode the known return type of the distributed invocation.

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
final func decodeReturnType() throws -> (any Any.Type)?
```

#### Discussion

It is legal to implement this by returning `nil`, and then the system will take the concrete return type from the located function signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationdecoder/decodereturntype())*