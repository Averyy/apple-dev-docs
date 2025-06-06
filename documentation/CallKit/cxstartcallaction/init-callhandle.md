# init(call:handle:)

**Framework**: CallKit  
**Kind**: init

Initializes a new action to start a call with the specified UUID to a recipient with the specified handle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(call callUUID: UUID, handle: CXHandle)
```

#### Return Value

A new action for the specified call UUID and handle.

## Parameters

- `callUUID`: The unique identifier for the associated   object.
- `handle`: The handle for the receipient, such as a phone number or email address.

## See Also

- [init?(coder: NSCoder)](cxstartcallaction/init(coder:).md)
  Creates a new action to start a call with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction/init(call:handle:))*