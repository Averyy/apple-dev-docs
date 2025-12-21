# propertiesChanged(properties:)

**Framework**: Core Audio  
**Kind**: method  
**Required**: Yes

Called when registered properties change.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func propertiesChanged(properties: [AudioObjectPropertyAddress])
```

#### Discussion

Listeners will be called when possibly many properties have changed. Consequently, the implementation of a listener must go through the array of addresses to see what exactly has changed. Note that the array of addresses will always have at least one address in it for which the listener is signed up to receive notifications about but may contain addresses for properties for which the listener is not signed up to receive notifications.

## Parameters

- `properties`: An array of AudioObjectPropertyAddresses indicating which properties changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/propertylistenerdelegate/propertieschanged(properties:))*