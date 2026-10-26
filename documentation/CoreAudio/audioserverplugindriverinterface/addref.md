# AddRef

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
unsigned int (*)(void *) AddRef;
```

#### Return Value

The resulting reference count after the new reference is added.

#### Discussion

The IUnknown method for retaining a reference to a CFPlugIn type.

## Parameters

- `inDriver`: The CFPlugIn type to retain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugindriverinterface/addref)*