# onThrow(error:)

**Framework**: Distributed  
**Kind**: method  
**Required**: Yes

Invoked when the distributed target execution of a target has thrown an error.

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
func onThrow<Err>(error: Err) async throws where Err : Error
```

#### Discussion

It is not guaranteed that the error conform to the [`SerializationRequirement`](distributedtargetinvocationresulthandler/serializationrequirement.md); This guarantee is only given to return values (and offered by `onReturn`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationresulthandler/onthrow(error:))*