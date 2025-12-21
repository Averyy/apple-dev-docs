# FromChain

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static IOCommand * FromChain(queue_chain_t * link);
```

#### Return Value

Queue used to queue commands.

#### Discussion

Given the queue_chain_t from CommandChain, return the IOCommand instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommand/fromchain)*