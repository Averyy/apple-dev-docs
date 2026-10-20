# init

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes the network packet buffer pool object.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual bool init();
```

#### Return Value

`YES` if initialization was successful, or `NO` if an error occurred.

## See Also

### Creating a Buffer Pool
- [Create](./create.md)
  Creates a new packet buffer pool object and allocates space for the specified number of packets.
- [free](./free.md)
  Releases the resources owned by the network packet buffer pool object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool/init)*