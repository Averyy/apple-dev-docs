# NSZombieEnabled

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A global variable related to zombie objects that in practice has no effect.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
extern BOOL NSZombieEnabled;
```

## See Also

### Diagnostics and Debugging
- [NSLog](./nslog.md)
  Logs an error message to the Apple System Log facility.
- [func NSLogv(String, CVaListPointer)](./nslogv%28_,_%29.md)
  Logs an error message to the Apple System Log facility.
- [NSDeallocateZombies](./nsdeallocatezombies.md)
  A global variable that determines whether or not the memory of zombie objects is deallocated.
- [NSDebugEnabled](./nsdebugenabled.md)
  A global variable that can be used to enable debug behavior in your app, such as extra logging.
- [NSKeepAllocationStatistics](./nskeepallocationstatistics.md)
  A no-longer-used global variable related to keeping statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nszombieenabled)*