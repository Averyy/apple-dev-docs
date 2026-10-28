# free

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Performs any final cleanup for the service.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual void free();
```

## Discussion

Use this method to perform any final cleanup of your service, such as deallocating any memory associated with your service. The system calls this method at some point after it calls your service’s [`Stop`](../../DriverKit/ioservice/stop.md) method.

## See Also

### Configuring the Driver Service
- [init](./init.md)
  Handles the basic initialization of the service.
- [RegisterEthernetInterface](./registerethernetinterface-4jqw8.md)
  Registers your driver with the networking stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/free)*