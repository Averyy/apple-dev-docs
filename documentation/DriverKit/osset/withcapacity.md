# withCapacity

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSSetPtr withCapacity(uint32_t capacity);
```

#### Return Value

NULL on failure, otherwise the allocated OSSet with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSSet object with preallocated capacity.

## Parameters

- `capacity`: Count of allocated capacity for members in array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osset/withcapacity)*