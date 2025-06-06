# OSReportWithBacktrace

**Framework**: DriverKit  
**Kind**: func

Generates a backtrace and message for debugging.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void OSReportWithBacktrace(const char * str, ...);
```

#### Discussion

Generates a backtrace and message for debugging. May be inoperative on release OS builds.

## Parameters

- `str`: Printf-Like arguments to be logged, along with the backtrace of the caller.

## See Also

- [OSSynchronizeIO](ossynchronizeio.md)
  Performs an `mfence` instruction on Intel-based Mac computers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osreportwithbacktrace)*