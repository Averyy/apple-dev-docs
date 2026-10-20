# layoutChildren(for:visualState:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

This function provides the layout of the direct children of this equipment and is called whenever the snapshot changes. Override it to provide a custom layout. The output of this function is considered to be only a function of its inputs. Reaching out to data outside what is provided might result in undefined behavior.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func layoutChildren(for snapshot: TableSnapshot, visualState: TableVisualState) -> any EquipmentLayout
```

## Default Implementations

### Equipment Implementations
- [func layoutChildren(for: TableSnapshot, visualState: TableVisualState) -> any EquipmentLayout](./layoutchildren%28for,visualstate%29-41c25.md)
  This function provides the layout of the direct children of this equipment and is called whenever the snapshot changes. Override it to provide a custom layout. The output of this function is considered to be only a function of its inputs. Reaching out to data outside what is provided might result in undefined behavior.

## See Also

### Displaying the equipment
- [func restingOrientation(state: Self.State) -> Rotation3D](./restingorientation%28state%29.md)
  The resting orientation of the equipment given the current State.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipment/layoutchildren(for:visualstate:))*