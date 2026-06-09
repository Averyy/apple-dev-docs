# init(processIdentifier:)

**Framework**: Foundation  
**Kind**: init

Creates and returns an application address descriptor using the specified process identifier.

**Availability**:
- macOS 10.11+

## Declaration

```swift
init(processIdentifier: pid_t)
```

#### Discussion

The result is suitable for use as the `targetDescriptor` parameter of `+appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(processidentifier:))*