# returnCommand

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void returnCommand(IOCommand * command);
```

#### Discussion

The returnCommand method is used to place an object of type IOCommand into the pool, whether it be the first time, or the 1000th time.

## Parameters

- `command`: The command to place in the pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommandpool/returncommand)*