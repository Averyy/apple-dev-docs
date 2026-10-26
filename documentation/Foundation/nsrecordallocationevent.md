# NSRecordAllocationEvent

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Notes an object or zone allocation event and various other statistics, such as the time and current thread.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
extern void NSRecordAllocationEvent(int eventType, id object);
```

## See Also

### Debugging
- [NSCountFrames](./nscountframes.md)
  Returns the number of call frames on the stack.
- [NSFrameAddress](./nsframeaddress.md)
  Returns the value of the frame pointer of the specified frame.
- [NSIsFreedObject](./nsisfreedobject.md)
  Returns a Boolean indicating whether the specified object has been freed.
- [NSReturnAddress](./nsreturnaddress.md)
  Returns the value of the return address of the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrecordallocationevent)*