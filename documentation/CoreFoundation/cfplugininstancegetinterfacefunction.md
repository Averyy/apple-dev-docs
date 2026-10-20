# CFPlugInInstanceGetInterfaceFunction

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Not recommended.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CFPlugInInstanceGetInterfaceFunction = (CFPlugInInstance?, CFString?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> DarwinBoolean
```

```c
typedef unsigned char (*)(struct __CFPlugInInstance *, const struct __CFString *, void **) CFPlugInInstanceGetInterfaceFunction;
```

## See Also

### Callbacks
- [typealias CFPlugInInstanceDeallocateInstanceDataFunction](./cfplugininstancedeallocateinstancedatafunction.md)
  Not recommended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugininstancegetinterfacefunction)*