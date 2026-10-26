# Release

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
unsigned int (*)(void *) Release;
```

#### Return Value

The resulting reference count after the reference has been removed.

#### Discussion

The IUnknown method for releasing a reference to a CFPlugIn type.

## Parameters

- `inDriver`: The CFPlugIn type to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/release)*