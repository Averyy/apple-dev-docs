# init(coder:)

**Framework**: CallKit  
**Kind**: init  
**Role**: Initializer

Creates a new action to play dual-tone multifrequency (DTMF) tones with data in an unarchiver.

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
- [init(call: UUID, digits: String, type: CXPlayDTMFCallAction.ActionType)](./init%28call,digits,type%29.md)
  Initializes a new action for a call identified by a given UUID, as well as a specified type and sequence of digits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/init(coder:))*