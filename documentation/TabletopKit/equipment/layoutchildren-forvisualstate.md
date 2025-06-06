# layoutChildren(for:visualState:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

This function provides the layout of the direct children of this equipment and is called whenever the snapshot changes. Override it to provide a custom layout. The output of this function is considered to be only a function of its inputs. Reaching out to data outside what is provided might result in undefined behavior.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func layoutChildren(for snapshot: TableSnapshot, visualState: TableVisualState) -> any EquipmentLayout
```

## See Also

- [func restingOrientation(state: Self.State) -> Rotation3D](equipment/restingorientation(state:).md)
  The resting orientation of the equipment given the current State.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipment/layoutchildren(for:visualstate:))*