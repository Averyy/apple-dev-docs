# init

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Handles the basic initialization of the service.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual bool init();
```

## Return Value

`YES` if initialization was successful, or `NO` if an error occurred.

## Discussion

The system calls this method shortly after it instantiates your [`IOUserNetworkEthernet`](../iousernetworkethernet.md) subclass, and before it calls the [`Start`](../../DriverKit/ioservice/start.md) method of your service. Limit the work you do in this method to simple tasks that must occur before your service stats. For example, you might use this method to allocate memory for your `ivars` structure.

Always call the `super` implementation of this method at some point.

## See Also

### Configuring the Driver Service
- [free](./free.md)
  Performs any final cleanup for the service.
- [RegisterEthernetInterface](./registerethernetinterface-4jqw8.md)
  Registers your driver with the networking stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/init)*