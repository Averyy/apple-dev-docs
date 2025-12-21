# AudioHardwareObject

**Framework**: Core Audio  
**Kind**: class

The audio HAL provides an abstraction through which applications can access audio hardware. To do this, the HAL provides a small set of audio objects that provide access to the various pieces of the system. Audio objects all have a set of properties that describe and manipulate their state. AudioHardwareObject is a base class for all other audio objects. As such, all classes inherit this set of properties.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
class AudioHardwareObject
```

## Topics

### Initializers
- [init(id: AudioObjectID)](audiohardwareobject/init(id:).md)
### Instance Properties
- [var baseClassID: AudioClassID](audiohardwareobject/baseclassid.md)
  An AudioClassID that identifies the class from which the class of the AudioObject is derived. This value must always be one of the standard classes.
- [var classID: AudioClassID](audiohardwareobject/classid.md)
  An AudioClassID that identifies the class of the AudioObject.
- [var creatorBundleID: String](audiohardwareobject/creatorbundleid.md)
  A String that contains the bundle ID of the plug-in that instantiated the object.
- [var delegates: [any PropertyListenerDelegate]](audiohardwareobject/delegates.md)
  An array of PropertyListenerDelegates used to notify property changes.
- [var firmwareVersion: String](audiohardwareobject/firmwareversion.md)
  A String that contains the human readable firmware version for the object.
- [let id: AudioObjectID](audiohardwareobject/id.md)
  A UInt32 that provides a handle on a specific AudioObject.
- [var isIdentifying: Bool](audiohardwareobject/isidentifying.md)
  A Bool where a value of true indicates that the object’s hardware is drawing attention to itself, typically by flashing or lighting up its front panel display. A value of false indicates that this function is turned off. This makes it easy for a user to associate the physical hardware with its representation in an application. Typically, this property is only supported by AudioHardwareDevices and AudioHardwareBoxes.
- [var manufacturer: String](audiohardwareobject/manufacturer.md)
  A String that contains the human readable name of the manufacturer of the hardware the object is a part of.
- [var modelName: String](audiohardwareobject/modelname.md)
  A String that contains the human readable model name of the object. The model name differs from name in that two objects of the same model will have the same value for this property but may have different values for name.
- [var name: String](audiohardwareobject/name.md)
  A String that contains the human readable name of the object.
- [var ownedObjects: [AudioHardwareObject]](audiohardwareobject/ownedobjects.md)
  An array of AudioHardwareObjects that represent all the objects owned by this object.
- [var owner: AudioHardwareObject?](audiohardwareobject/owner.md)
  An AudioHardwareObject that identifies this object’s owner. Note that all AudioHardwareObject are owned by some other AudioHardwareObject. The only exception is the AudioSystemObject, for which the value of this property is nil.
- [var serialNumber: String](audiohardwareobject/serialnumber.md)
  A String that contains the human readable serial number for the object.
### Instance Methods
- [func addListener(forProperties: [AudioObjectPropertyAddress], dispatchQueue: dispatch_queue_t?) throws](audiohardwareobject/addlistener(forproperties:dispatchqueue:).md)
  Registers for notifications to be received on the property listener delegates when the given properties change.
- [func hasProperty(address: AudioObjectPropertyAddress) -> Bool](audiohardwareobject/hasproperty(address:).md)
  Queries an AudioHardwareObject about whether or not it has the given property.
- [func isPropertySettable(address: AudioObjectPropertyAddress) throws -> Bool](audiohardwareobject/ispropertysettable(address:).md)
  Queries an AudioHardwareObject about whether or not the given property can be set using setPropertyValue.
- [func propertyData(address: AudioObjectPropertyAddress, qualifier: Data?) throws -> Data](audiohardwareobject/propertydata(address:qualifier:).md)
  Queries an AudioHardwareObject to get the data of the given property.
- [func propertyDataSize(address: AudioObjectPropertyAddress, qualifier: Data?) throws -> Int](audiohardwareobject/propertydatasize(address:qualifier:).md)
  Queries an AudioHardwareObject to find the size of the data for the given property.
- [func removeListener(forProperties: [AudioObjectPropertyAddress], dispatchQueue: dispatch_queue_t?) throws](audiohardwareobject/removelistener(forproperties:dispatchqueue:).md)
  Unregisters for receiving notifications when the given properties change.
- [func setCreatorBundleID(String) throws](audiohardwareobject/setcreatorbundleid(_:).md)
  Set the creatorBundleID property.
- [func setIsIdentifying(Bool) throws](audiohardwareobject/setisidentifying(_:).md)
  Set the isIdentifying property.
- [func setName(String) throws](audiohardwareobject/setname(_:).md)
  Set the name property.
- [func setPropertyData(address: AudioObjectPropertyAddress, qualifier: Data?, data: Data) throws](audiohardwareobject/setpropertydata(address:qualifier:data:)-4kzgv.md)
  Tells an AudioObject to change the value of the given property using the  provided data.
- [func setPropertyData(address: AudioObjectPropertyAddress, qualifier: Data?, data: inout Data) async throws](audiohardwareobject/setpropertydata(address:qualifier:data:)-7cfn.md)
  Tells an AudioObject to change the value of the given property using the  provided data.

## Relationships

### Inherited By
- [AudioHardwareBox](audiohardwarebox.md)
- [AudioHardwareClock](audiohardwareclock.md)
- [AudioHardwareControl](audiohardwarecontrol.md)
- [AudioHardwarePlugin](audiohardwareplugin.md)
- [AudioHardwareProcess](audiohardwareprocess.md)
- [AudioHardwareStream](audiohardwarestream.md)
- [AudioHardwareSystem](audiohardwaresystem.md)
- [AudioHardwareTap](audiohardwaretap.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject)*