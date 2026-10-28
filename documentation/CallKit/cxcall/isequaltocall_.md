# isEqualToCall:

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a given call is equal to the receiver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```objc
- (BOOL) isEqualToCall:(CXCall *) call;
```

## Return Value

[`true`](../../Swift/true.md) if `call` is equal to the receiver, otherwise [`false`](../../Swift/false.md).

## Parameters

- `call`: The call with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcall/isequaltocall:)*