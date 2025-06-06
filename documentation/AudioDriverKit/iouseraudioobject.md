# IOUserAudioObject

**Framework**: AudioDriverKit  
**Kind**: class

The base class for most classes in the framework.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioObject;
```

#### Overview

All classes in the framework subclass [`IOUserAudioObject`](iouseraudioobject.md), except for [`IOUserAudioDriver`](iouseraudiodriver.md), which subclasses [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) from [`DriverKit`](https://developer.apple.com/documentation/DriverKit).

Don’t subclass or instantiate [`IOUserAudioObject`](iouseraudioobject.md) directly.

## Topics

### Creating an Audio Object
- [init](iouseraudioobject/init-1ar2z.md)
  Initializes an instance of the audio object base class.
- [init](iouseraudioobject/init-26qwx.md)
  Initializes an empty object.
### Freeing an Audio Object
- [free](iouseraudioobject/free.md)
  Frees the audio object.
### Getting Information About the Class
- [GetClassID](iouseraudioobject/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudioobject/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetObjectID](iouseraudioobject/getobjectid.md)
  Gets the object’s identifier.
- [IOUserAudioObjectID](audiodriverkit/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [GetWorkQueue](iouseraudioobject/getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.
### Working with Object Names
- [GetName](iouseraudioobject/getname.md)
  Gets the name of the object.
- [SetName](iouseraudioobject/setname.md)
  Sets the name of the object.
### Using Custom Properties
- [AddCustomProperty](iouseraudioobject/addcustomproperty.md)
  Adds a custom property to the audio object.
- [RemoveCustomProperty](iouseraudioobject/removecustomproperty.md)
  Removes a previously-added custom property object from the audio object.
- [IOUserAudioCustomProperty](iouseraudiocustomproperty.md)
  A custom property to associate with audio objects.
### Instance Methods
- [GetElementCategoryName](iouseraudioobject/getelementcategoryname.md)
- [GetElementName](iouseraudioobject/getelementname.md)
- [GetElementNumberName](iouseraudioobject/getelementnumbername.md)
- [GetOwnerObjectID](iouseraudioobject/getownerobjectid.md)
- [SetElementCategoryName](iouseraudioobject/setelementcategoryname.md)
- [SetElementName](iouseraudioobject/setelementname.md)
- [SetElementNumberName](iouseraudioobject/setelementnumbername.md)

## Relationships

### Inherits From
- [OSObject](../DriverKit/OSObject.md)
### Inherited By
- [IOUserAudioBox](iouseraudiobox.md)
- [IOUserAudioClockDevice](iouseraudioclockdevice.md)
- [IOUserAudioControl](iouseraudiocontrol.md)
- [IOUserAudioCustomProperty](iouseraudiocustomproperty.md)
- [IOUserAudioStream](iouseraudiostream.md)

## See Also

- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
- [DriverKit Audio Family](../BundleResources/Entitlements/com.apple.developer.driverkit.family.audio.md)
  A Boolean value that indicates whether the device supports audio functionality.
- [Creating an audio device driver](creating-an-audio-device-driver.md)
  Implement a configurable audio input source as a driver extension that runs in user space in macOS and iPadOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject)*