# type

**Framework**: PushKit  
**Kind**: property  
**Role**: Instance Property

The push type constant associated with the token.

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

### Getting the Token
- [var token: Data](./token.md)
  A unique device token to use when sending push notifications to the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushcredentials/type)*