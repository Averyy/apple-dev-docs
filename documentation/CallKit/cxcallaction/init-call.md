# init(call:)

**Framework**: CallKit  
**Kind**: init

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

#### Return Value

A new action for the specified call UUID.

## Parameters

- `callUUID`: The unique identifier for the associated   object.

## See Also

- [init?(coder: NSCoder)](cxcallaction/init(coder:).md)
  Creates a new action for a call with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxcallaction/init(call:))*