# selectorItemKind(fromID:)

**Framework**: Core Audio  
**Kind**: method

This property returns a UInt32 that identifies the kind of selector item the item ID refers to.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func selectorItemKind(fromID ID: UInt32) throws -> UInt32
```

#### Return Value

A UInt32 that identifies the kind of selector item the item ID refers to.

#### Discussion

This property is optional for selector controls and that the meaning of the value depends on the specific subclass being queried.

## Parameters

- `ID`: A UInt32 containing the ID of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarecontrol/selectoritemkind(fromid:))*