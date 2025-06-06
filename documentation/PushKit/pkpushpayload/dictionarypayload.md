# dictionaryPayload

**Framework**: PushKit  
**Kind**: property

The contents of the received payload.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var dictionaryPayload: [AnyHashable : Any] { get }
```

#### Discussion

For VoIP pushes, the sender is free to specify any fields for the contained data as long as it is provided in a text-encodable JSON format.

## See Also

- [var type: PKPushType](pkpushpayload/type.md)
  The type value indicating how to interpret the payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushpayload/dictionarypayload)*