# isSupported

**Framework**: RoomPlan  
**Kind**: property

A Boolean value that indicates whether the user’s device supports the framework.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 16.0+

## Declaration

```swift
static var isSupported: Bool { get }
```

#### Discussion

Before attempting to begin a session, ensure the user’s device supports room scanning. This property is `true` if the device contains a LiDAR Scanner; otherwise, `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roomcapturesession/issupported)*