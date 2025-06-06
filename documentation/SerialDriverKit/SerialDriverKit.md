# SerialDriverKit

**Framework**: Serialdriverkit  
**Kind**: module

Develop drivers for serial I/O devices connected to your Mac.

**Availability**:
- DriverKit 19.0+

#### Overview

The SerialDriverKit framework supports the development of drivers for devices that communicate using a serial interface. The framework lets you build drivers to support modem hardware or a universal asynchronous receiver/transmitter (UART). To create a driver that communicates serially with a USB device, use the [`USBSerialDriverKit`](https://developer.apple.com/documentation/USBSerialDriverKit) framework instead.

Package your driver in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade the driver on the user’s Mac.

> **Note**:  SerialDriverKit is available on macOS.

## Topics

### Samples
- [DriverKit sample code](../DriverKit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Serial Interface
- [com.apple.developer.driverkit.family.serial](../BundleResources/Entitlements/com.apple.developer.driverkit.family.serial.md)
  A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.
- [IOUserSerial](iouserserial.md)
  The class for building a service that communicates using a serial connection.
### Reference
- [SerialDriverKit Enumerations](serialdriverkit-enumerations.md)
- [SerialDriverKit Data Types](serialdriverkit-data-types.md)
### Namespaces
- [driverkit](driverkit.md)
### Macros
- [PD_RS232_S_LE](pd_rs232_s_le.md)
- [PD_RS232_S_RNG](pd_rs232_s_rng.md)
- [kIOTTYBaseNameKey](kiottybasenamekey.md)
- [kIOTTYSuffixKey](kiottysuffixkey.md)
### Enumeration Cases
- [kIOSerialMemoryArena](kioserialmemoryarena.md)
- [kIOSerialMemoryRxBuf](kioserialmemoryrxbuf.md)
- [kIOSerialMemoryTxBuf](kioserialmemorytxbuf.md)
- [kIOSerialPTYMaster](kioserialptymaster.md)
- [kIOSerialUserClient](kioserialuserclient.md)
- [kIOSerialUserClientIoctl](kioserialuserclientioctl.md)
- [kIOSerialUserClientOpen](kioserialuserclientopen.md)
- [kIOSerialUserClientPoll](kioserialuserclientpoll.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SerialDriverKit)*