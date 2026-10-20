# init(coder:)

**Framework**: CallKit  
**Kind**: init  
**Role**: Initializer

Creates a new action for a call with data in an unarchiver.

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

### Creating New Call Actions
- [init(call: UUID)](./init%28call%29.md)
  Initializes a new action for a call identified by a given UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallaction/init(coder:))*