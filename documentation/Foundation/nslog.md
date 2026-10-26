# NSLog

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Logs an error message to the Apple System Log facility.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void NSLog(NSString *format, ...);
```

#### Discussion

Simply calls [`NSLogv(_:_:)`](./nslogv%28_,_%29.md), passing it a variable number of arguments.

## See Also

### Diagnostics and Debugging
- [func NSLogv(String, CVaListPointer)](./nslogv%28_,_%29.md)
  Logs an error message to the Apple System Log facility.
- [NSDeallocateZombies](./nsdeallocatezombies.md)
  A global variable that determines whether or not the memory of zombie objects is deallocated.
- [NSDebugEnabled](./nsdebugenabled.md)
  A global variable that can be used to enable debug behavior in your app, such as extra logging.
- [NSZombieEnabled](./nszombieenabled.md)
  A global variable related to zombie objects that in practice has no effect.
- [NSKeepAllocationStatistics](./nskeepallocationstatistics.md)
  A no-longer-used global variable related to keeping statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslog)*