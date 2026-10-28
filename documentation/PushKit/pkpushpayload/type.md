# type

**Framework**: PushKit  
**Kind**: property  
**Role**: Instance Property

The type value indicating how to interpret the payload.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var type: PKPushType { get }
```

```objc
@property (copy, readonly) PKPushType type;
```

## Discussion

For possible values, see [`PKPushType`](../pkpushtype.md).

## See Also

### Payload Data
- [var dictionaryPayload: [AnyHashable : Any]](./dictionarypayload.md)
  The contents of the received payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushpayload/type)*