# FromChain

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static IOCommand * FromChain(queue_chain_t *link);
```

## Return Value

Queue used to queue commands.

## Discussion

Given the queue_chain_t from CommandChain, return the IOCommand instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommand/fromchain)*