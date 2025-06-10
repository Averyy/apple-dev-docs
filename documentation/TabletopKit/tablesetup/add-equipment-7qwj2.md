# add(equipment:)

**Framework**: TabletopKit  
**Kind**: method

Add the given equipment to the table setup.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
mutating func add<E>(equipment: E) where E : Equipment, E.State : BitwiseCopyable, E.State : CustomEquipmentState
```

## Parameters

- `equipment`: The equipment to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesetup/add(equipment:)-7qwj2)*