# QueryInterface

**Framework**: Core Audio  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
int (*)(void *, CFUUIDBytes, void **) QueryInterface;
```

## Return Value

An error code indicating success of failure.

## Discussion

The IUnknown method for interface discovery.

## Parameters

- `inDriver`: The CFPlugIn type to query.
- `inUUID`: The UUID of the interface to find.
- `outInterface`: The returned interface or NULL if none was found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/queryinterface)*