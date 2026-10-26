# NSDeallocateZombies

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A global variable that determines whether or not the memory of zombie objects is deallocated.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
extern BOOL NSDeallocateZombies;
```

## See Also

### Diagnostics and Debugging
- [NSLog](./nslog.md)
  Logs an error message to the Apple System Log facility.
- [func NSLogv(String, CVaListPointer)](./nslogv%28_,_%29.md)
  Logs an error message to the Apple System Log facility.
- [NSDebugEnabled](./nsdebugenabled.md)
  A global variable that can be used to enable debug behavior in your app, such as extra logging.
- [NSZombieEnabled](./nszombieenabled.md)
  A global variable related to zombie objects that in practice has no effect.
- [NSKeepAllocationStatistics](./nskeepallocationstatistics.md)
  A no-longer-used global variable related to keeping statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdeallocatezombies)*