# IOUserNetworkPacketBufferPool

**Framework**: NetworkingDriverKit  
**Kind**: class

An object that manages the storage space for packets coming into and out of your driver.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserNetworkPacketBufferPool;
```

#### Overview

Create an [`IOUserNetworkPacketBufferPool`](iousernetworkpacketbufferpool.md) during the initial setup of your driver and use it to store the packets that your driver transmits or receives. Every driver must have a packet buffer pool large enough to hold all of the packets in its transmit and receive queues. You allocate this pool early in the [`Start`](https://developer.apple.com/documentation/DriverKit/IOService/Start) method of your [`IOUserNetworkEthernet`](iousernetworkethernet.md) service, and you deallocate that pool only after your service stops.

## Topics

### Creating a Buffer Pool
- [Create](iousernetworkpacketbufferpool/create.md)
  Creates a new packet buffer pool object and allocates space for the specified number of packets.
- [init](iousernetworkpacketbufferpool/init.md)
  Initializes the network packet buffer pool object.
- [free](iousernetworkpacketbufferpool/free.md)
  Releases the resources owned by the network packet buffer pool object.
### Getting Pool Information
- [GetBufferCount](iousernetworkpacketbufferpool/getbuffercount.md)
  Returns the number of buffers associated with the network packet buffer pool.
- [GetPacketCount](iousernetworkpacketbufferpool/getpacketcount.md)
  Returns the number of network packets that the pool is capable of storing.
### Deallocating Packets
- [DeallocatePacket](iousernetworkpacketbufferpool/deallocatepacket-3i02n.md)
  Disposes of any resources associated with the packet and makes the packet available for reuse.
- [DeallocatePackets](iousernetworkpacketbufferpool/deallocatepackets-186ya.md)
  Disposes of any resources associated with the specified packets and makes them available for reuse.
### Getting the Memory Block
- [CopyMemoryDescriptor](iousernetworkpacketbufferpool/copymemorydescriptor.md)
  Returns a memory descriptor for the buffer pool’s contents.
### Instance Methods
- [allocatePacket](iousernetworkpacketbufferpool/allocatepacket.md)
- [deallocatePacket](iousernetworkpacketbufferpool/deallocatepacket-42aob.md)
- [deallocatePackets](iousernetworkpacketbufferpool/deallocatepackets-58i5.md)
- [getPoolOwnerDevice](iousernetworkpacketbufferpool/getpoolownerdevice.md)
- [initWithName](iousernetworkpacketbufferpool/initwithname.md)
- [newPacket](iousernetworkpacketbufferpool/newpacket.md)
- [release](iousernetworkpacketbufferpool/release.md)
### Type Methods
- [CreateWithOptions](iousernetworkpacketbufferpool/createwithoptions.md)
- [withName](iousernetworkpacketbufferpool/withname.md)

## Relationships

### Inherits From
- [OSObject](../DriverKit/OSObject.md)

## See Also

- [IOUserNetworkPacket](iousernetworkpacket.md)
  A network packet containing the data for your driver to process.
- [IOUserNetworkPacketDirection](iousernetworkpacketdirection.md)
  The direction in which the packet moves, relative to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool)*