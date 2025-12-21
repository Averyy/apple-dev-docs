# hasProperty(address:)

**Framework**: Core Audio  
**Kind**: method

Queries an AudioHardwareObject about whether or not it has the given property.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func hasProperty(address: AudioObjectPropertyAddress) -> Bool
```

#### Return Value

A Bool indicating whether or not the AudioHardwareObject has the given property.

## Parameters

- `address`: An AudioObjectPropertyAddress indicating which property is being queried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/hasproperty(address:))*