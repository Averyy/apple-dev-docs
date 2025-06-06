# IOUserSerial

**Framework**: SerialDriverKit  
**Kind**: class

The class for building a service that communicates using a serial connection.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
class IOUserSerial;
```

#### Overview

Subclass `IOUserSerial` and use it to implement a service for communicating with serial devices. This class automatically manages the buffers used to store incoming and outgoing data. You are responsible for configuring your hardware, and for reading and writing data at appropriate times. This class supports configuration through standard modem commands or using universal asynchronous receiver/transmitter (UART) hardware.

If your driver communicates with your device over USB, subclass [`IOUserUSBSerial`](https://developer.apple.com/documentation/USBSerialDriverKit/IOUserUSBSerial) (in the USBSerialDriverKit framework) instead of this class.

## Topics

### Configuring the Service
- [init](iouserserial/init.md)
  Handles the basic initialization of the service.
- [Start](iouserserial/start.md)
  Starts the current service and associates it with the specified provider.
- [Stop](iouserserial/stop.md)
  Stops the service associated with the specified provider.
- [free](iouserserial/free.md)
  Performs any final cleanup for the service.
- [initWith](iouserserial/initwith.md)
  Initializes the private data structures associated with this class.
### Activating and Deactivating the Service
- [HwActivate](iouserserial/hwactivate.md)
  Opens the communication channel to the device.
- [HwDeactivate](iouserserial/hwdeactivate.md)
  Closes the communication channel to the device.
### Configuring the Serial Data Queues
- [ConnectQueues](iouserserial/connectqueues.md)
  Creates and configures the buffers that store the data moving to and from the device.
- [DisconnectQueues](iouserserial/disconnectqueues.md)
  Releases the buffers that manage data moving to and from the device.
### Programming the Modem
- [HwGetModemStatus](iouserserial/hwgetmodemstatus.md)
  Gets the current status of the modem from the hardware.
- [SetModemStatus](iouserserial/setmodemstatus.md)
  Sets the modem status to the specified values.
- [HwResetFIFO](iouserserial/hwresetfifo.md)
  Sends a command to reset the specified device queues.
- [HwSendBreak](iouserserial/hwsendbreak.md)
  Sends a linebreak command to the device.
- [HwProgramBaudRate](iouserserial/hwprogrambaudrate.md)
  Sets the communication baud rate to the specified value.
- [HwProgramLatencyTimer](iouserserial/hwprogramlatencytimer.md)
  Sets the amount of time to wait before sending the current buffer to the device.
- [HwProgramMCR](iouserserial/hwprogrammcr.md)
  Configure the setings for the device’s modem control register (MCR).
- [HwProgramUART](iouserserial/hwprogramuart.md)
  Configure the settings for the device’s universal asynchronous receiver/transmitter (UART).
- [Hardware Constants](hardware-constants.md)
  Configure your device with the appropriate parity and flow-control options.
### Transmitting and Receiving Data
- [RxDataAvailable](iouserserial/rxdataavailable.md)
  Notifies the system that data from the device is now available.
- [RxFreeSpaceAvailable](iouserserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](iouserserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [TxFreeSpaceAvailable](iouserserial/txfreespaceavailable.md)
  Notifies the system that the device is ready to accept more data.
- [RxError](iouserserial/rxerror.md)
  Reports errors that occurred when receiving data from the device.
### Instance Methods
- [HwProgramFlowControl](iouserserial/hwprogramflowcontrol.md)

## See Also

- [com.apple.developer.driverkit.family.serial](../BundleResources/Entitlements/com.apple.developer.driverkit.family.serial.md)
  A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/serialdriverkit/iouserserial)*