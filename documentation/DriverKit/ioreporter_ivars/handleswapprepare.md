# handleSwapPrepare

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
IOReturn handleSwapPrepare(int newNChannels);
```

#### Return Value

IOReturn code

#### Discussion

::handleSwapPrepare() is responsible for allocating appropriately- sized buffers (based on the new number of channels) and storing them in _swap* instance variables.  If returning and error, it must deallocate any buffers and set to NULL any _swap* variables.

Locking: The caller must ensure that the  lock is HELD but that the reporter (data) lock is .

## Parameters

- `newNChannels`: Target number of channels


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/handleswapprepare)*