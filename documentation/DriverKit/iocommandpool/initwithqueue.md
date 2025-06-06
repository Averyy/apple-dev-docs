# initWithQueue

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool initWithQueue(IODispatchQueue * queue);
```

#### Return Value

Returns true if command pool was successfully initialized.

#### Discussion

```None
         Should probably use IOCommandPool::withQueue() as it is easier to use.
```

## Parameters

- `queue`: The IODispatchQueue that this command pool should synchronize with.   This queue must have been allocated with the kIODispatchQueueReentrant   option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iocommandpool/initwithqueue)*