# CFFileDescriptorEnableCallBacks(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Enables callbacks for a given CFFileDescriptor.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFFileDescriptorEnableCallBacks(_ f: CFFileDescriptor!, _ callBackTypes: CFOptionFlags)
```

```c
extern void CFFileDescriptorEnableCallBacks(CFFileDescriptorRef f, CFOptionFlags callBackTypes);
```

## Parameters

- `f`: A CFFileDescriptor.
- `callBackTypes`: A bitmask that specifies which callbacks to enable (see [Callback Identifiers](./api-1477595-callback-identifiers.md) for possible components).

## See Also

### Managing Callbacks
- [func CFFileDescriptorDisableCallBacks(CFFileDescriptor!, CFOptionFlags)](./cffiledescriptordisablecallbacks%28_,_%29.md)
  Disables callbacks for a given CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorenablecallbacks(_:_:))*