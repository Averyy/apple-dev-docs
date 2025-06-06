# CheckForWork

**Framework**: DriverKit  
**Kind**: method

Checks for events to handle.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t CheckForWork(bool synchronous);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

Don’t override this method or call it from your own code. Existing dispatch source objects implement this method internally and use it to generate new events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iodispatchsource/checkforwork)*