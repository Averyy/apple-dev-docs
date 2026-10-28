# init(call:)

**Framework**: CallKit  
**Kind**: init  
**Role**: Initializer

Initializes a new action for a call identified by a given UUID.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(call callUUID: UUID)
```

```objc
- (instancetype) initWithCallUUID:(NSUUID *) callUUID;
```

## Return Value

A new action for the specified call UUID.

## Parameters

- `callUUID`: The unique identifier for the associated [`CXCall`](../cxcall.md) object.

## See Also

### Creating New Call Actions
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a new action for a call with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallaction/init(call:))*