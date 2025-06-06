# init(coder:)

**Framework**: CallKit  
**Kind**: init

Creates a new action to start a call with data in an unarchiver.

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

## Parameters

- `aDecoder`: An unarchiver object.

## See Also

- [init(call: UUID, handle: CXHandle)](cxstartcallaction/init(call:handle:).md)
  Initializes a new action to start a call with the specified UUID to a recipient with the specified handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction/init(coder:))*