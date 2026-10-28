# callUUIDToGroupWith

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the call to be grouped with the call associated with the receiver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var callUUIDToGroupWith: UUID? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSUUID * callUUIDToGroupWith;
```

## Discussion

If `nil`, the call associated with the receiver leaves any group it’s currently a member of.

If the call associated with the receiver is already in a group, the call should first leave that group, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction/calluuidtogroupwith)*