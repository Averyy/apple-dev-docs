# cp_time_wait_until

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Blocks the current thread until the specified time.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_time_wait_until(cp_time_t time);
```

## Mentions

- [Drawing fully immersive content using Metal](./drawing-fully-immersive-content-using-metal.md)

## Parameters

- `time`: The Mach absolute time at which to wake up the thread. Typically, you supply one of the predicted times associated with the current frame, such as the optimal input time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_time_wait_until)*