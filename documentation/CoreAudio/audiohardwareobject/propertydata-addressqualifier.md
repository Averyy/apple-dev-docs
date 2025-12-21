# propertyData(address:qualifier:)

**Framework**: Core Audio  
**Kind**: method

Queries an AudioHardwareObject to get the data of the given property.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func propertyData(address: AudioObjectPropertyAddress, qualifier: Data? = nil) throws -> Data
```

#### Return Value

A buffer containing the data for the given property

## Parameters

- `address`: An AudioObjectPropertyAddress indicating which property is being queried.
- `qualifier`: A buffer of data to be used in determining the data of the property being   queried. Note that not all properties require qualification, in which case this value   will be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/propertydata(address:qualifier:))*