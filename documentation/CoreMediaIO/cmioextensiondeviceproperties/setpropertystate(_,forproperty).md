# setPropertyState(_:forProperty:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Sets the value of a device property.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func setPropertyState(_ propertyState: CMIOExtensionPropertyState<AnyObject>?, forProperty property: CMIOExtensionProperty)
```

```objc
- (void) setPropertyState:(CMIOExtensionPropertyState *) propertyState forProperty:(CMIOExtensionProperty) property;
```

#### Discussion

Setting a `nil` property state value doesn’t remove the property.

## Parameters

- `propertyState`: The updated property state.
- `property`: The property to update.

## See Also

### Configuring Device Properties
- [var model: String?](./model.md)
  A device model string.
- [var linkedCoreAudioDeviceUID: String?](./linkedcoreaudiodeviceuid.md)
  A universal identifier of the audio device linked to this device.
- [var transportType: Int?](./transporttype-96gm.md)
  The transport type of the device, such as USB or HDMI.
- [var suspended: Bool?](./suspended-eru0.md)
  A Boolean value that indicates whether the device is in a suspended state.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./propertiesdictionary.md)
  A dictionary of properties for a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/setpropertystate(_:forproperty:))*