# setPropertyData(address:qualifier:data:)

**Framework**: Core Audio  
**Kind**: method

Tells an AudioObject to change the value of the given property using the  provided data.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func setPropertyData(address: AudioObjectPropertyAddress, qualifier: Data? = nil, data: Data) throws
```

#### Discussion

Note that the value of the property should not be considered changed until the HAL has called the listeners as many properties values are changed asynchronously.

## Parameters

- `address`: An AudioObjectPropertyAddress indicating which property is being changed.
- `qualifier`: A buffer of data to be used in determining the data of the property being   set. Note that not all properties require qualification, in which case this value   will be nil.
- `data`: The buffer containing the data to be used to change the property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/setpropertydata(address:qualifier:data:)-4kzgv)*