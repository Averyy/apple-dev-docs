# IOUserAudioDriver

**Framework**: AudioDriverKit  
**Kind**: class

A DriverKit provider object that manages communications with an audio device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioDriver;
```

#### Overview

For the Core Audio host to match against this driver, add the following keys to `IOKitPersonalities`, in the driver’s `Info.plist` file:

```swift
 <key>IOUserAudioDriverUserClientProperties</key>
 <dict>
     <key>IOClass</key>
     <string>IOUserUserClient</string>
     <key>IOUserClass</key>
     <string>IOUserAudioDriverUserClient</string>
 </dict>
```

After matching the host with the driver, the AudioDriverKit framework creates the connection to the Core Audio HAL as soon as the [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) calls [`NewUserClient`](iouseraudiodriver/newuserclient.md). The driver extension must have the `com.apple.developer.driverkit.allow-any-userclient-access` entitlement.

## Topics

### Running the Driver Service
- [init](iouseraudiodriver/init.md)
  Handles the basic initialization of the service.
- [Start](iouseraudiodriver/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouseraudiodriver/stop.md)
  Stops the service associated with the specified provider.
- [free](iouseraudiodriver/free.md)
  Performs any final cleanup for the service.
### Getting Information About the Class
- [GetClassID](iouseraudiodriver/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiodriver/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
- [GetWorkQueue](iouseraudiodriver/getworkqueue.md)
  Gets the work queue created by the audio object, as a pointer to a dispatch queue.
- [GetName](iouseraudiodriver/getname.md)
  Gets the name of the driver.
- [SetName](iouseraudiodriver/setname.md)
  Sets the name of the driver.
### Getting the Driver’s Audio Object Identifier
- [kIOUserAudioObjectIDDriver](audiodriverkit/kiouseraudioobjectiddriver.md)
  The audio object ID of the driver.
### Starting and Stopping the Driver
- [StartDevice](iouseraudiodriver/startdevice.md)
  Tells the driver to start I/O on an audio device or audio clock device.
- [StopDevice](iouseraudiodriver/stopdevice.md)
  Tells the driver to stop I/O on an audio device or audio clock device.
- [IOUserAudioObjectID](audiodriverkit/iouseraudioobjectid.md)
  An identifier that provides a handle on a specific audio object.
- [IOUserAudioStartStopFlags](audiodriverkit/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.
### Creating a New Client
- [NewUserClient](iouseraudiodriver/newuserclient.md)
  Requests the creation of a new user client for the service.
### Working with Transport Type
- [GetTransportType](iouseraudiodriver/gettransporttype.md)
  Gets the transport type of the driver.
- [SetTransportType](iouseraudiodriver/settransporttype.md)
  Set the transport type of the driver.
- [IOUserAudioTransportType](audiodriverkit/iouseraudiotransporttype.md)
  The type of transport to deliver audio.
### Working with Audio Objects
- [AddObject](iouseraudiodriver/addobject.md)
  Adds an audio object to the driver.
- [RemoveObject](iouseraudiodriver/removeobject.md)
  Removes an audio object from the driver.
- [GetAudioObjectForObjectID](iouseraudiodriver/getaudioobjectforobjectid.md)
  Gets a pointer to an audio object, given the object’s identifier.
### Communicating with the Host
- [PropertiesChanged](iouseraudiodriver/propertieschanged.md)
  Informs the host when the state of an object in the driver changes.
- [IOUserAudioObjectPropertySelector](audiodriverkit/iouseraudioobjectpropertyselector.md)
  A four character code which, along with the scope and element, specific piece of information about an audio object.
### Working with Custom Properties
- [AddCustomProperty](iouseraudiodriver/addcustomproperty.md)
  Adds a custom property object to the driver.
- [RemoveCustomProperty](iouseraudiodriver/removecustomproperty.md)
  Removes a previously-added custom property object from the driver.
- [IOUserAudioCustomProperty](iouseraudiocustomproperty.md)
  A custom property to associate with audio objects.

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)

## See Also

- [IOUserAudioObject](iouseraudioobject.md)
  The base class for most classes in the framework.
- [DriverKit Audio Family](../BundleResources/Entitlements/com.apple.developer.driverkit.family.audio.md)
  A Boolean value that indicates whether the device supports audio functionality.
- [Creating an audio device driver](creating-an-audio-device-driver.md)
  Implement a configurable audio input source as a driver extension that runs in user space in macOS and iPadOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver)*