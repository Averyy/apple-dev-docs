# NSReturnAddress

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns the value of the return address of the specified frame.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
extern void *NSReturnAddress(NSUInteger frame);
```

## See Also

### Debugging
- [NSCountFrames](./nscountframes.md)
  Returns the number of call frames on the stack.
- [NSFrameAddress](./nsframeaddress.md)
  Returns the value of the frame pointer of the specified frame.
- [NSIsFreedObject](./nsisfreedobject.md)
  Returns a Boolean indicating whether the specified object has been freed.
- [NSRecordAllocationEvent](./nsrecordallocationevent.md)
  Notes an object or zone allocation event and various other statistics, such as the time and current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsreturnaddress)*