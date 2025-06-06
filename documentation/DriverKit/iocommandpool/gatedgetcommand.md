# gatedGetCommand

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t gatedGetCommand(IOCommand * * command, bool blockForCommand);
```

#### Return Value

kIOReturnNoResources if no command is available and the client doesn’t wish to block until one does become available. kIOReturnSuccess if the vCommand argument is valid.

#### Discussion

The gatedGetCommand method is used to serialize the extraction of a command from the pool synchronized with the pool’s queue.

## Parameters

- `command`: A pointer to a pointer to an IOCommand object where the returned   command will be stored.
- `blockForCommand`: A bool that indicates whether to block the request until a command   becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommandpool/gatedgetcommand)*