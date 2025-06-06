# gatedReturnCommand

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t gatedReturnCommand(IOCommand * command);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

The gatedReturnCommand method is used to serialize the return of a command to the pool synchronized with the pool’s queue.

## Parameters

- `command`: A pointer to the IOCommand object to be returned to the pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommandpool/gatedreturncommand)*