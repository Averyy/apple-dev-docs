# free

**Framework**: NetworkingDriverKit  
**Kind**: method

Performs any final cleanup for the service.

**Availability**:
- DriverKit ?+

## Declaration

```swift
void free();
```

#### Discussion

Use this method to perform any final cleanup of your service, such as deallocating any memory associated with your service. The system calls this method at some point after it calls your service’s [`Stop`](https://developer.apple.com/documentation/kernel/ioservice/3180713-stop) method.

## See Also

- [init](iousernetworkethernet/init.md)
  Handles the basic initialization of the service.
- [RegisterEthernetInterface](iousernetworkethernet/registerethernetinterface-4jqw8.md)
  Registers your driver with the networking stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/free)*