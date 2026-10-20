# init(call:muted:)

**Framework**: CallKit  
**Kind**: init  
**Role**: Initializer

Initializes a new action for a call identified by a given UUID, as well as whether the call is muted.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
convenience init(call callUUID: UUID, muted: Bool)
```

```objc
- (instancetype) initWithCallUUID:(NSUUID *) callUUID muted:(BOOL) muted;
```

#### Return Value

A new action for the specified call UUID and whether the call is muted.

## Parameters

- `callUUID`: The unique identifier for the associated [`CXCall`](../cxcall.md) object of the action.
- `muted`: Whether the call is muted.

## See Also

### Creating New Actions
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new action for a call with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetmutedcallaction/init(call:muted:))*