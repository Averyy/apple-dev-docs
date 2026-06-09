# currentProcess()

**Framework**: Foundation  
**Kind**: method

Creates and returns an application address descriptor using the current process.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class func currentProcess() -> NSAppleEventDescriptor
```

#### Discussion

The result is suitable for use as the `targetDescriptor` parameter of `+appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/currentprocess())*