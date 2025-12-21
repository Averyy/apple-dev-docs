# propertyDataSize(address:qualifier:)

**Framework**: Core Audio  
**Kind**: method

Queries an AudioHardwareObject to find the size of the data for the given property.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func propertyDataSize(address: AudioObjectPropertyAddress, qualifier: Data? = nil) throws -> Int
```

#### Return Value

An Int  indicating how many bytes the data for the given property occupies.

## Parameters

- `address`: An AudioObjectPropertyAddress indicating which property is being queried.
- `qualifier`: A buffer of data to be used in determining the data of the property being   queried. Note that not all properties require qualification, in which case this value   will be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/propertydatasize(address:qualifier:))*