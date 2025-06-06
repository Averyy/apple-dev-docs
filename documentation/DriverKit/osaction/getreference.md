# GetReference

**Framework**: DriverKit  
**Kind**: method

Returns a pointer to any additional memory allocated by the action object on your behalf.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void * GetReference();
```

## Mentions

- [Creating a Driver Using the DriverKit SDK](creating-a-driver-using-the-driverkit-sdk.md)

#### Return Value

A pointer to the additional storage you requested at creation time. This method returns `NULL` if you passed `0` to the `referenceSize` parameter of the [`Create`](https://developer.apple.com/documentation/kernel/osaction/3438206-create) method. It also returns `NULL` if the action object doesn’t belong to the current process.

#### Discussion

The action object zero-initializes the memory it allocates. Only the process that owns the action object may access the memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osaction/getreference)*