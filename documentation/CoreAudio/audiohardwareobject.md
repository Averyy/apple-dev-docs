# AudioHardwareObject

**Framework**: Core Audio  
**Kind**: class

**Availability**:
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
- [var classID: AudioClassID](audiohardwareobject/classid.md)
- [var creatorBundleID: String](audiohardwareobject/creatorbundleid.md)
- [var delegates: [any PropertyListenerDelegate]](audiohardwareobject/delegates.md)
- [var firmwareVersion: String](audiohardwareobject/firmwareversion.md)
- [let id: AudioObjectID](audiohardwareobject/id.md)
- [var isIdentifying: Bool](audiohardwareobject/isidentifying.md)
- [var manufacturer: String](audiohardwareobject/manufacturer.md)
- [var modelName: String](audiohardwareobject/modelname.md)
- [var name: String](audiohardwareobject/name.md)
- [var ownedObjects: [AudioHardwareObject]](audiohardwareobject/ownedobjects.md)
- [var owner: AudioHardwareObject?](audiohardwareobject/owner.md)
- [var serialNumber: String](audiohardwareobject/serialnumber.md)
### Instance Methods
- [func addListener(forProperties: [AudioObjectPropertyAddress], dispatchQueue: dispatch_queue_t?) throws](audiohardwareobject/addlistener(forproperties:dispatchqueue:).md)
- [func hasProperty(address: AudioObjectPropertyAddress) -> Bool](audiohardwareobject/hasproperty(address:).md)
- [func isPropertySettable(address: AudioObjectPropertyAddress) throws -> Bool](audiohardwareobject/ispropertysettable(address:).md)
- [func propertyData(address: AudioObjectPropertyAddress, qualifier: Data?) throws -> Data](audiohardwareobject/propertydata(address:qualifier:).md)
- [func propertyDataSize(address: AudioObjectPropertyAddress, qualifier: Data?) throws -> Int](audiohardwareobject/propertydatasize(address:qualifier:).md)
- [func removeListener(forProperties: [AudioObjectPropertyAddress], dispatchQueue: dispatch_queue_t?) throws](audiohardwareobject/removelistener(forproperties:dispatchqueue:).md)
- [func setCreatorBundleID(String) throws](audiohardwareobject/setcreatorbundleid(_:).md)
- [func setIsIdentifying(Bool) throws](audiohardwareobject/setisidentifying(_:).md)
- [func setName(String) throws](audiohardwareobject/setname(_:).md)
- [func setPropertyData(address: AudioObjectPropertyAddress, qualifier: Data?, data: Data) throws](audiohardwareobject/setpropertydata(address:qualifier:data:)-4kzgv.md)
- [func setPropertyData(address: AudioObjectPropertyAddress, qualifier: Data?, data: inout Data) async throws](audiohardwareobject/setpropertydata(address:qualifier:data:)-7cfn.md)

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