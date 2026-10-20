# init(coder:)

**Framework**: CallKit  
**Kind**: init  
**Role**: Initializer

Creates a new action to place a call on hold with data in an unarchiver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Parameters

- `aDecoder`: An unarchiver object.

## See Also

### Creating New Actions
- [init(call: UUID, onHold: Bool)](./init%28call,onhold%29.md)
  Initializes a new action for a call identified by a given UUID, as well as whether the call is on hold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetheldcallaction/init(coder:))*