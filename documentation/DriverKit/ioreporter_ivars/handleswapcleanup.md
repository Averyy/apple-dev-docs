# handleSwapCleanup

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void handleSwapCleanup(int swapNChannels);
```

#### Discussion

::handleSwapCleanup() is responsible for deallocating the buffers no longer used after a swap.  It must always be called if SwapPrepare() completes successfully.  Because bufers may be swapped in and out of existance, the _swap* variables may be NULL and should be set to NULL when complete.

Locking: The caller must ensure that the  lock is HELD but that the reporter (data) lock is .

## Parameters

- `swapNChannels`: Channel-Relative size of the _swap buffers


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioreporter_ivars/handleswapcleanup)*