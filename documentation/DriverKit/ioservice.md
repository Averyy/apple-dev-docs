# IOService

**Framework**: DriverKit  
**Kind**: class

The base class for managing the setup and registration of your driver.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOService;
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Overview

An [`IOService`](ioservice.md) object is the base class the system uses to represent all devices and device-related interfaces. When the user plugs in a device, the system creates one or more service objects to manage interactions with that device. One service object represents the device itself, and additional service objects represent the interfaces or communication protocols that the device supports. For example, the driver for a USB camera that supports multiple video and audio protocols might define different service objects for each protocol.

When the user plugs in a device, the system looks for the service objects that best match the device’s capabilities. Apple’s built-in driver families support most device types and a large array of standard interfaces. You provide custom service objects to support your device’s custom behaviors.

In most cases, you subclass a child of [`IOService`](ioservice.md) such as [`IOUSBHostInterface`](https://developer.apple.com/documentation/USBDriverKit/IOUSBHostInterface), instead of [`IOService`](ioservice.md) itself. Use the methods of this class to do the following:

- Handle the initialization, setup, and teardown of your driver.
- View and manage the I/O Registry entry for the device or interface.
- Configure the dispatch queue on which to execute your code.
- Respond to power-level changes

For additional information about how to implement services for a particular type of device, see the service subclasses in [`HIDDriverKit`](https://developer.apple.com/documentation/HIDDriverKit), [`USBDriverKit`](https://developer.apple.com/documentation/USBDriverKit), [`NetworkingDriverKit`](https://developer.apple.com/documentation/NetworkingDriverKit), [`SerialDriverKit`](https://developer.apple.com/documentation/SerialDriverKit), and [`USBSerialDriverKit`](https://developer.apple.com/documentation/USBSerialDriverKit).

##### Adding Member Variables to Your Custom Subclass

Don’t declare custom member variables directly in your [`IOService`](ioservice.md) subclass. Instead, DriverKit requires you to define all variables in a separate structure. During initialization, allocate a block of memory for that structure and assign that block to the system-provided `ivars` variable of your service class. The following code example shows you how to define the structure and allocate it in the [`init`](ioservice/init.md) method of your service class.

```objc
struct MyCustomKeyboardDriver_IVars
{
    OSArray *elements;
    
    struct {
        OSArray *elements;
    } keyboard;
};

bool MyCustomKeyboardDriver::init()
{
   if (!super::init()) {return false;}
    
   // Allocate memory for the instance variables.
   ivars = IONewZero(MyCustomKeyboardDriver_IVars, 1);
   if (!ivars) {return false;}
    
exit:
   return true;
}

```

Deallocate any memory that you allocate for your custom variables in the [`free`](ioservice/free.md) method of your class.

## Topics

### Running the Service
- [init](ioservice/init.md)
  Handles the basic initialization of the service.
- [Start](ioservice/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](ioservice/stop.md)
  Stops the service associated with the specified provider.
- [free](ioservice/free.md)
  Performs any final cleanup for the service.
### Registering the Service with IOKit
- [RegisterService](ioservice/registerservice.md)
  Starts the registration process for the service and performs any additional matching.
- [SetName](ioservice/setname.md)
  Sets the name of the service in the system’s registry.
- [GetRegistryEntryID](ioservice/getregistryentryid.md)
  Returns the registry ID for the current service.
- [IOServiceName](ioservicename.md)
  A string type for setting the name of the service in the system’s registry.
### Managing the Registry Properties
- [CopyProperties](ioservice/copyproperties.md)
  Returns the registry properties associated with the current service.
- [SetProperties](ioservice/setproperties.md)
  Sends the dictionary of properties to the current service object.
- [SearchProperty](ioservice/searchproperty.md)
  Searches for a property with the specified name in the current service or one of its parent services, and returns the corresponding value.
- [IOPropertyName](iopropertyname.md)
  A string type for specifying the name of a property in the system’s registry.
- [IORegistryPlaneName](ioregistryplanename.md)
  A string type for specifying the name of a plane in the system’s registry.
- [Search Options](3325572-search_options.md)
  Options to apply when searching for registry properties.
### Configuring Additional Dispatch Queues
- [SetDispatchQueue](ioservice/setdispatchqueue.md)
  Associates a custom dispatch queue with the service and assigns the specified name to it.
- [CopyDispatchQueue](ioservice/copydispatchqueue.md)
  Gets the dispatch queue with the specified name from the current service.
### Responding to Power-Level Changes
- [SetPowerState](ioservice/setpowerstate.md)
  Updates the service in response to power-related changes for a provider.
- [ChangePowerState](ioservice/changepowerstate.md)
  Changes the device’s power state to the specified level.
- [Service Power Capabilities](3325571-service_power_capabilities.md)
  Constants that indicate the power state of a device.
### Creating a New Service
- [NewUserClient](ioservice/newuserclient.md)
  Requests the creation of a new user client for the service.
- [Create](ioservice/create.md)
  Requests the creation of a new service object.
### Instance Methods
- [AdjustBusy](ioservice/adjustbusy.md)
- [ClientCrashed](ioservice/clientcrashed.md)
- [ConfigureReport](ioservice/configurereport.md)
- [CopyName](ioservice/copyname.md)
- [CopyProviderProperties](ioservice/copyproviderproperties.md)
- [CopySystemStateNotificationService](ioservice/copysystemstatenotificationservice.md)
- [CoreAnalyticsSendEvent](ioservice/coreanalyticssendevent.md)
- [CreateDefaultDispatchQueue](ioservice/createdefaultdispatchqueue.md)
- [GetBusyState](ioservice/getbusystate.md)
- [GetProvider](ioservice/getprovider.md)
- [JoinPMTree](ioservice/joinpmtree.md)
- [RemoveProperty](ioservice/removeproperty.md)
- [RequireMaxBusStall](ioservice/requiremaxbusstall.md)
- [SetLegend](ioservice/setlegend.md)
- [SetPowerOverride](ioservice/setpoweroverride.md)
- [StateNotificationItemCopy](ioservice/statenotificationitemcopy.md)
- [StateNotificationItemCreate](ioservice/statenotificationitemcreate.md)
- [StateNotificationItemSet](ioservice/statenotificationitemset.md)
- [Stop_async](ioservice/stop_async.md)
- [StringFromReturn](ioservice/stringfromreturn.md)
- [Terminate](ioservice/terminate.md)
- [UpdateReport](ioservice/updatereport.md)
### Type Methods
- [CreateKernelClassMatchingDictionary](ioservice/createkernelclassmatchingdictionary-9b28.md)
- [CreateKernelClassMatchingDictionary](ioservice/createkernelclassmatchingdictionary-3uqly.md)
- [CreateNameMatchingDictionary](ioservice/createnamematchingdictionary-2nzta.md)
- [CreateNameMatchingDictionary](ioservice/createnamematchingdictionary-206ej.md)
- [CreatePropertyMatchingDictionary](ioservice/createpropertymatchingdictionary-4tuca.md)
- [CreatePropertyMatchingDictionary](ioservice/createpropertymatchingdictionary-6o4ss.md)
- [CreateUserClassMatchingDictionary](ioservice/createuserclassmatchingdictionary-4gpbj.md)
- [CreateUserClassMatchingDictionary](ioservice/createuserclassmatchingdictionary-60ptx.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)
### Inherited By
- [IOUserClient](iouserclient.md)
- [IOUserServer](iouserserver.md)

## See Also

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)
  Create a driver that supports proprietary features of your company’s hardware devices.
- [Debugging and testing system extensions](debugging-and-testing-system-extensions.md)
  Debug your system extensions by temporarily disabling the security checks that macOS performs during the installation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice)*