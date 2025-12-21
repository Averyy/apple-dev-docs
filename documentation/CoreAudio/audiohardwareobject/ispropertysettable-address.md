# isPropertySettable(address:)

**Framework**: Core Audio  
**Kind**: method

Queries an AudioHardwareObject about whether or not the given property can be set using setPropertyValue.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func isPropertySettable(address: AudioObjectPropertyAddress) throws -> Bool
```

#### Return Value

A Bool indicating whether or not the property is settable.

## Parameters

- `address`: An AudioObjectPropertyAddress indicating which property is being queried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/ispropertysettable(address:))*