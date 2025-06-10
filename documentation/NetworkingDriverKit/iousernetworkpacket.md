# IOUserNetworkPacket

**Framework**: NetworkingDriverKit  
**Kind**: class

A network packet containing the data for your driver to process.

**Availability**:
- DriverKit ?+

## Declaration

```swift
class IOUserNetworkPacket;
```

#### Overview

An [`IOUserNetworkPacket`](iousernetworkpacket.md) contains meta information about a network packet being trasmitted to or from your device. You do not create network packets directly. Instead, you dequeue them from an appropriate submission queue, such as an [`IOUserNetworkRxSubmissionQueue`](iousernetworkrxsubmissionqueue.md). You a packet object to get the length of the packet data and the location of that data in its memory buffer, accommodating for any extra headroom bytes at the beginning of the packet.

## Topics

### Configuring the Network Packet
- [init](iousernetworkpacket/init.md)
  Initializes the network packet object.
- [free](iousernetworkpacket/free.md)
  Performs any final cleanup for the network packet.
### Configuring the Packet State Information
- [SetHeadroom](iousernetworkpacket/setheadroom.md)
  Changes the number of bytes to reserve at the front of the packet’s buffer to the specified value.
- [SetLinkHeaderLength](iousernetworkpacket/setlinkheaderlength-9fqmg.md)
  Changes the number of bytes to use for the link header to the specified value.
- [SetDataOffset](iousernetworkpacket/setdataoffset-16kx3.md)
  Changes the offset to the beginning of the packet’s data to the specified value.
- [SetDataLength](iousernetworkpacket/setdatalength-788b.md)
  Changes the number of bytes of data in the packet to the specified value.
### Getting the Packet Information
- [GetHeadroom](iousernetworkpacket/getheadroom.md)
  Gets the number of bytes reserved at the front of the packet’s buffer.
- [GetLinkHeaderLength](iousernetworkpacket/getlinkheaderlength-8dlhu.md)
  Gets the number of bytes to use for the link header.
- [GetDataOffset](iousernetworkpacket/getdataoffset-4tw7y.md)
  Gets the offset to the beginning of the packet’s data.
- [GetDataLength](iousernetworkpacket/getdatalength-8km3n.md)
  Gets the number of bytes of data in the packet.
- [GetMemorySegmentOffset](iousernetworkpacket/getmemorysegmentoffset-39e4c.md)
  Gets the offset to the beginning of the packet in the corresponding memory buffer.
### Getting the Packet’s Buffer Pool
- [GetPacketBufferPool](iousernetworkpacket/getpacketbufferpool-63snl.md)
  Gets the memory buffer that contains the pakcet.
### Instance Methods
- [clearTimestamp](iousernetworkpacket/cleartimestamp.md)
- [getDataIOVirtualAddress](iousernetworkpacket/getdataiovirtualaddress.md)
- [getDataLength](iousernetworkpacket/getdatalength-1niks.md)
- [getDataOff](iousernetworkpacket/getdataoff.md)
- [getDataOffset](iousernetworkpacket/getdataoffset-2h6cf.md)
- [getDataVirtualAddress](iousernetworkpacket/getdatavirtualaddress.md)
- [getExpiryTime](iousernetworkpacket/getexpirytime.md)
- [getLinkHeaderLength](iousernetworkpacket/getlinkheaderlength-3gau2.md)
- [getMSS](iousernetworkpacket/getmss.md)
- [getMemorySegmentOffset](iousernetworkpacket/getmemorysegmentoffset-2nuj3.md)
- [getPacketBufferPool](iousernetworkpacket/getpacketbufferpool-5dqqj.md)
- [getRxChecksumInfo](iousernetworkpacket/getrxchecksuminfo.md)
- [getServiceClass](iousernetworkpacket/getserviceclass.md)
- [getTSOInfo](iousernetworkpacket/gettsoinfo.md)
- [getTimestamp](iousernetworkpacket/gettimestamp.md)
- [getTraceID](iousernetworkpacket/gettraceid.md)
- [getTxChecksumInfo](iousernetworkpacket/gettxchecksuminfo.md)
- [getTxCsumFlags](iousernetworkpacket/gettxcsumflags.md)
- [getVlanTag](iousernetworkpacket/getvlantag.md)
- [initWithPool](iousernetworkpacket/initwithpool.md)
- [isLinkBroadcast](iousernetworkpacket/islinkbroadcast.md)
- [isLinkMulticast](iousernetworkpacket/islinkmulticast.md)
- [isTimestampRequested](iousernetworkpacket/istimestamprequested.md)
- [isTransportTrafficBackground](iousernetworkpacket/istransporttrafficbackground.md)
- [isTransportTrafficRealtime](iousernetworkpacket/istransporttrafficrealtime.md)
- [prepareWithQueue](iousernetworkpacket/preparewithqueue.md)
- [setCompletionStatus](iousernetworkpacket/setcompletionstatus.md)
- [setDataLength](iousernetworkpacket/setdatalength-9uo6r.md)
- [setDataOff](iousernetworkpacket/setdataoff.md)
- [setDataOffAndLen](iousernetworkpacket/setdataoffandlen.md)
- [setDataOffset](iousernetworkpacket/setdataoffset-459jc.md)
- [setDataOffsetAndLength](iousernetworkpacket/setdataoffsetandlength.md)
- [setIsLinkMulticast](iousernetworkpacket/setislinkmulticast.md)
- [setLROInfo](iousernetworkpacket/setlroinfo.md)
- [setLinkHeaderLength](iousernetworkpacket/setlinkheaderlength-23dbd.md)
- [setRxChecksumInfo](iousernetworkpacket/setrxchecksuminfo.md)
- [setTimestamp](iousernetworkpacket/settimestamp.md)
- [setVlanTag](iousernetworkpacket/setvlantag.md)
- [setWakeFlag](iousernetworkpacket/setwakeflag.md)
- [traceEvent](iousernetworkpacket/traceevent.md)
### Type Methods
- [withPool](iousernetworkpacket/withpool.md)

## Relationships

### Inherits From
- [OSObject](../DriverKit/OSObject.md)

## See Also

- [IOUserNetworkPacketBufferPool](iousernetworkpacketbufferpool.md)
  An object that manages the storage space for packets coming into and out of your driver.
- [IOUserNetworkPacketDirection](iousernetworkpacketdirection.md)
  The direction in which the packet moves, relative to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket)*