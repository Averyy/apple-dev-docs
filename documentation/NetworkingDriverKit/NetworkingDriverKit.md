# NetworkingDriverKit

**Framework**: NetworkingDriverKit  
**Kind**: module

Develop drivers for Ethernet networking devices.

**Availability**:
- DriverKit 19.0+

#### Overview

Use NetworkingDriverKit to develop drivers for USB Ethernet adapters. This framework extends the API of [`DriverKit`](https://developer.apple.com/documentation/DriverKit), providing you with a service class for managing your networking driver. It also provides support for managing the memory you use to store packets, transferring those packets between the device and networking stack, and inspecting the Ethernet link status.

Note that Ethernet is the only networking interface currently supported by NetworkingDriverKit.

Develop your driver with DriverKit and NetworkingDriverKit. Use USBDriverKit to manage the connection to your hardware device. Include your driver inside your macOS app and use the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade the driver on the user’s Mac.

> **Note**:  NetworkingDriverKit is available on macOS.

## Topics

### Essentials
- [com.apple.developer.driverkit.family.networking](../BundleResources/Entitlements/com.apple.developer.driverkit.family.networking.md)
  A Boolean value that indicates whether to match the driver against devices that communicate using networking protocols.
### Samples
- [Connecting a network driver](../pcidriverkit/connecting_a_network_driver.md)
  Create an Ethernet driver that interfaces with the system’s network protocol stack.
- [DriverKit sample code](../DriverKit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Network Service
- [IOUserNetworkEthernet](iousernetworkethernet.md)
  The object you use to manage the setup, configuration, and teardown of your networking driver.
### Packet Management
- [IOUserNetworkPacketBufferPool](iousernetworkpacketbufferpool.md)
  An object that manages the storage space for packets coming into and out of your driver.
- [IOUserNetworkPacket](iousernetworkpacket.md)
  A network packet containing the data for your driver to process.
- [IOUserNetworkPacketDirection](iousernetworkpacketdirection.md)
  The direction in which the packet moves, relative to the device.
### Packet Queues
- [IOUserNetworkRxSubmissionQueue](iousernetworkrxsubmissionqueue.md)
  The queue that receives packets from the device.
- [IOUserNetworkRxCompletionQueue](iousernetworkrxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the networking stack.
- [IOUserNetworkTxSubmissionQueue](iousernetworktxsubmissionqueue.md)
  The queue that receives packets from the networking stack.
- [IOUserNetworkTxCompletionQueue](iousernetworktxcompletionqueue.md)
  The queue you use to store packets that you successfully transferred to the device.
- [IOUserNetworkPacketQueue](iousernetworkpacketqueue.md)
  The base class for the queues that manage the packets moving to and from your device.
### Reference
- [NetworkingDriverKit Structures](networkingdriverkit-structures.md)
- [NetworkingDriverKit Data Types](networkingdriverkit-data-types.md)
- [NetworkingDriverKit Constants](networkingdriverkit-constants.md)
### Classes
- [IOUserNetworkPacketPoller](iousernetworkpacketpoller.md)
- [IOUserNetworkPacketQueueCompat](iousernetworkpacketqueuecompat.md)
- [IOUserNetworkRxCompletionQueueCompat](iousernetworkrxcompletionqueuecompat.md)
- [IOUserNetworkRxSubmissionQueueCompat](iousernetworkrxsubmissionqueuecompat.md)
- [IOUserNetworkTxCompletionQueueCompat](iousernetworktxcompletionqueuecompat.md)
- [IOUserNetworkTxSubmissionQueueCompat](iousernetworktxsubmissionqueuecompat.md)
### Structures
- [IOUserNetworkEthernet_IVars](iousernetworkethernet_ivars.md)
- [IOUserNetworkPacketQueueCompat_IVars](iousernetworkpacketqueuecompat_ivars.md)
- [IOUserNetworkRxCompletionQueueCompat_IVars](iousernetworkrxcompletionqueuecompat_ivars.md)
- [IOUserNetworkRxSubmissionQueueCompat_IVars](iousernetworkrxsubmissionqueuecompat_ivars.md)
- [IOUserNetworkTxCompletionQueueCompat_IVars](iousernetworktxcompletionqueuecompat_ivars.md)
- [IOUserNetworkTxSubmissionQueueCompat_IVars](iousernetworktxsubmissionqueuecompat_ivars.md)
### Macros
- [NDK_25](ndk_25.md)
### Enumeration Cases
- [kIOUserNetworkHWAssistLRONumSeg](kiousernetworkhwassistlronumseg.md)
### Type Aliases
- [DequeueActionCompat](dequeueactioncompat.md)
- [EnqueueActionCompat](enqueueactioncompat.md)
- [IOUserNetworkPacketQueueCompatId](iousernetworkpacketqueuecompatid.md)
- [QueryFreeSpaceActionCompat](queryfreespaceactioncompat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/NetworkingDriverKit)*