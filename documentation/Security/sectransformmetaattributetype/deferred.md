# SecTransformMetaAttributeType.deferred

**Framework**: Security  
**Kind**: case  
**Role**: Case

The attribute defers notifications.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
case deferred
```

```c
kSecTransformMetaAttributeDeferred
```

#### Discussion

Determines if the AttributeSetNotification notification or the ProcessData blocks are deferred until [`SecTransformExecute(_:_:)`](../sectransformexecute%28_,_%29.md) is called. This metadata value has a default value of [`true`](../../Swift/true.md) for the input attribute but is [`false`](../../Swift/false.md) for all other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/deferred)*