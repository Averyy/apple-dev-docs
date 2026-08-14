# SecTransformMetaAttributeType.deferred

**Framework**: Security  
**Kind**: case

The attribute defers notifications.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case deferred
```

#### Discussion

Determines if the AttributeSetNotification notification or the ProcessData blocks are deferred until [`SecTransformExecute(_:_:)`](sectransformexecute(_:_:).md) is called. This metadata value has a default value of [`true`](https://developer.apple.com/documentation/swift/true) for the input attribute but is [`false`](https://developer.apple.com/documentation/swift/false) for all other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/deferred)*