# restingOrientation(state:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

The resting orientation of the equipment given the current State.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func restingOrientation(state: Self.State) -> Rotation3D
```

## See Also

- [func layoutChildren(for: TableSnapshot, visualState: TableVisualState) -> any EquipmentLayout](equipment/layoutchildren(for:visualstate:).md)
  This function provides the layout of the direct children of this equipment and is called whenever the snapshot changes. Override it to provide a custom layout. The output of this function is considered to be only a function of its inputs. Reaching out to data outside what is provided might result in undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipment/restingorientation(state:))*