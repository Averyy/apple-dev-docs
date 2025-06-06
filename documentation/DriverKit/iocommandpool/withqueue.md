# withQueue

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static IOCommandPoolPtr withQueue(IODispatchQueue * queue);
```

#### Discussion

```None
         a new instance of an IOCommandPool and returns a pointer to that object.
```

## Parameters

- `queue`: The IODispatchQueue that this command pool should synchronize with.   This queue must have been allocated with the kIODispatchQueueReentrant   option.   Returns a pointer to an instance of IOCommandPool if successful,   otherwise NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommandpool/withqueue)*