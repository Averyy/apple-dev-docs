# accessories

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The collection of accessories in the room.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var accessories: [HMAccessory] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<HMAccessory *> * accessories;
```

#### Discussion

You assign accessories to a room using the [`assignAccessory(_:to:completionHandler:)`](../hmhome/assignaccessory%28_,to,completionhandler%29.md) method of [`HMHome`](../hmhome.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmroom/accessories)*