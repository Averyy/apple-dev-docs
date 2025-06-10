# add(equipment:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
mutating func add<E>(equipment: E) where E : EntityEquipment, E.State : BitwiseCopyable, E.State : CustomEquipmentState
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesetup/add(equipment:)-294gb)*