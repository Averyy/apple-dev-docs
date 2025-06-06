# DriverKit

**Framework**: DriverKit  
**Kind**: module

Develop device drivers that run in user space.

**Availability**:
- DriverKit 19.0+
- iOS 16.0+
- iPadOS 16.0+
- macOS 10.15+

## Mentions

- [Creating drivers for iPadOS](creating-drivers-for-ipados.md)

#### Overview

The DriverKit framework defines the fundamental behaviors for device drivers in macOS and iPadOS. The C++ classes of this framework define your driver’s basic structure, and provide support for handling events and allocating memory. This framework also supports appropriate types for examining the numbers, strings, and other types of data in your driver’s I/O registry entry. Other frameworks, such as [`USBDriverKit`](https://developer.apple.com/documentation/USBDriverKit), [`HIDDriverKit`](https://developer.apple.com/documentation/HIDDriverKit), [`NetworkingDriverKit`](https://developer.apple.com/documentation/NetworkingDriverKit), [`PCIDriverKit`](https://developer.apple.com/documentation/PCIDriverKit), [`SerialDriverKit`](https://developer.apple.com/documentation/SerialDriverKit), and [`AudioDriverKit`](https://developer.apple.com/documentation/AudioDriverKit), provide the specific behaviors you need to support different types of devices.

The drivers you build with DriverKit run in user space, rather than as kernel extensions, which improves system stability and security. You create your driver as an app extension and deliver it inside your existing app.

In macOS, use the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade your driver. In iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

> **Note**:  The base DriverKit framework is available in macOS for Apple silicon and Intel-based Mac computers, and in iPadOS for devices with an M-series chip. The availability of family frameworks like [`USBDriverKit`](https://developer.apple.com/documentation/USBDriverKit) and [`AudioDriverKit`](https://developer.apple.com/documentation/AudioDriverKit) varies by platform.

 The base DriverKit framework is available in macOS for Apple silicon and Intel-based Mac computers, and in iPadOS for devices with an M-series chip. The availability of family frameworks like [`USBDriverKit`](https://developer.apple.com/documentation/USBDriverKit) and [`AudioDriverKit`](https://developer.apple.com/documentation/AudioDriverKit) varies by platform.

## Topics

### Essentials
- [Implementing drivers, system extensions, and kexts](../kernel/implementing_drivers_system_extensions_and_kexts.md)
  Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks. 
- [Creating drivers for iPadOS](creating-drivers-for-ipados.md)
  Bring your drivers to iPadOS by using the platform’s DriverKit support.
### Entitlements
- [Requesting Entitlements for DriverKit Development](requesting-entitlements-for-driverkit-development.md)
  Request the entitlement for DriverKit development, and request other entitlements your driver needs to interact with specific devices and interfaces.
- [com.apple.developer.driverkit](../BundleResources/Entitlements/com.apple.developer.driverkit.md)
  A Boolean value that indicates whether your extension has permission to run as a user-space driver.
- [com.apple.developer.driverkit.userclient-access](../BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [com.apple.developer.driverkit.allow-any-userclient-access](../BundleResources/Entitlements/com.apple.developer.driverkit.allow-any-userclient-access.md)
  A Boolean value that determines whether a macOS driver accepts user client connections from any application.
- [Communicates with Drivers](../BundleResources/Entitlements/com.apple.developer.driverkit.communicates-with-drivers.md)
  A Boolean value that indicates whether an iPadOS app can communicate with drivers.
- [DriverKit Allow Third Party User Clients](../BundleResources/Entitlements/com.apple.developer.driverkit.allow-third-party-userclients.md)
  A Boolean value that indicates whether an iPadOS driver accepts calls from third-party user clients.
### Samples
- [DriverKit sample code](driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Services
- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)
  Create a driver that supports proprietary features of your company’s hardware devices.
- [Debugging and testing system extensions](debugging-and-testing-system-extensions.md)
  Debug your system extensions by temporarily disabling the security checks that macOS performs during the installation process.
- [IOService](ioservice.md)
  The base class for managing the setup and registration of your driver.
### Event management
- [IODispatchQueue](iodispatchqueue.md)
  An object that manages the serial execution of blocks.
- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
  A dispatch source that reports hardware-related interrupt events to your driver.
- [IOTimerDispatchSource](iotimerdispatchsource.md)
  A dispatch source that notifies your driver at a specific time.
- [IODataQueueDispatchSource](iodataqueuedispatchsource.md)
  A dispatch source that manages a shared-memory data queue.
- [IODispatchSource](iodispatchsource.md)
  The common base class for dispatch sources.
- [OSAction](osaction.md)
  An object that executes your driver’s custom behavior.
### Memory management
- [IOBufferMemoryDescriptor](iobuffermemorydescriptor.md)
  A memory buffer allocated in the caller’s address space.
- [IOMemoryDescriptor](iomemorydescriptor.md)
  The base class for describing a location in memory.
- [IOMemoryMap](iomemorymap.md)
  A reference to an existing block of memory in the current process or in a different process.
- [Memory Utilities](memory-utilities.md)
  Allocate and deallocate memory and manage memory pointers in different address spaces.
### Registry data types
- [OSArray](osarray.md)
  A container for an ordered, random-access collection of objects.
- [OSDictionary](osdictionary.md)
  A container for a collection with elements that are key-value pairs.
- [OSBoolean](osboolean.md)
  A container for a true or false value.
- [OSData](osdata.md)
  A container for untyped data.
- [OSNumber](osnumber.md)
  A container for an integer value.
- [OSString](osstring.md)
  A container for managing an array of characters.
- [OSSerialization](osserialization.md)
  A container for one or more objects, serialized in a binary data format that is suitable for messaging.
- [OSCollection](oscollection.md)
  The base class for DriverKit collection objects.
- [OSContainer](oscontainer.md)
  The base class for DriverKit data objects.
- [OSObject](osobject.md)
  The base class for DriverKit objects
- [OSSymbol](ossymbol.md)
  A container for managing an array of characters.
- [IOFixed](iofixed.md)
  A fixed-point number.
### External drivers
- [IOUserClient](iouserclient.md)
  A connection to another service that the system manages.
- [IOUserServer](iouserserver.md)
  A system-managed service.
- [com.apple.developer.driverkit.userclient-access](../BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access.md)
  An array of strings that represent macOS driver extensions that may communicate with other DriverKit services.
- [Communicating between a DriverKit extension and a client app](communicating-between-a-driverkit-extension-and-a-client-app.md)
  Send and receive different kinds of data securely by validating inputs and asynchronously by storing and using a callback.
### Runtime support
- [OSDynamicCast](osdynamiccast.md)
  Casts an object safely to the specified type, if possible.
- [OSRequiredCast](osrequiredcast.md)
  Casts the object to the specified type, stopping the process if the object isn’t of the correct type.
- [IMPL](impl.md)
  Tells the system that the superclass implementation of this method runs in the kernel.
- [TYPE](type.md)
  Annotates a method declaration to indicate that it conforms to an existing method signature.
- [QUEUENAME](queuename.md)
  Tells the system to execute a method on the dispatch queue with the specified name.
- [SUPERDISPATCH](superdispatch.md)
  Tells the system to execute the superclass’ implementation of the current method in the kernel.
- [IIG_KERNEL](iig_kernel.md)
  Tells the system that the class or method runs inside the kernel.
- [LOCAL](local.md)
  Tells the system that the method runs locally in the driver extension’s process space.
- [LOCALONLY](localonly.md)
  Tells the system that the class or method runs locally in the driver extension’s process space.
- [Error Codes](error-codes.md)
  Determine the reason an operation fails.
- [C++ Runtime Support](c-runtime-support.md)
  Examine low-level types that DriverKit uses to support kernel-level operations.
### Classes
- [IOHistogramReporter](iohistogramreporter.md)
- [IOReportLegend](ioreportlegend.md)
- [IOReporter](ioreporter.md)
- [IOServiceStateNotificationDispatchSource](ioservicestatenotificationdispatchsource.md)
- [IOSimpleReporter](iosimplereporter.md)
- [IOStateReporter](iostatereporter.md)
- [OSBundle](osbundle.md)
- [OSMappedFile](osmappedfile.md)
### Reference
- [DriverKit Structures](driverkit-structures.md)
- [DriverKit Enumerations](driverkit-enumerations.md)
- [DriverKit Constants](driverkit-constants.md)
- [DriverKit Functions](driverkit-functions.md)
- [DriverKit Data Types](driverkit-data-types.md)
- [DriverKit Namespaces](driverkit-namespaces.md)
### Macros
- [Macros](driverkit-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/DriverKit)*