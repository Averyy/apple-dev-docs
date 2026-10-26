# NSIsFreedObject

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean indicating whether the specified object has been freed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
extern BOOL NSIsFreedObject(id anObject);
```

## See Also

### Debugging
- [NSCountFrames](./nscountframes.md)
  Returns the number of call frames on the stack.
- [NSFrameAddress](./nsframeaddress.md)
  Returns the value of the frame pointer of the specified frame.
- [NSRecordAllocationEvent](./nsrecordallocationevent.md)
  Notes an object or zone allocation event and various other statistics, such as the time and current thread.
- [NSReturnAddress](./nsreturnaddress.md)
  Returns the value of the return address of the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsisfreedobject)*