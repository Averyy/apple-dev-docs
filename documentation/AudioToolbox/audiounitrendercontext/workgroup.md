# workgroup

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The workgroup that manages the rendering threads of the audio unit.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```c
os_workgroup_t workgroup;
```

## Discussion

The value of this property might be `NULL` when the new render context does not perform real-time rendering. It might also be `NULL` when the new real-time render thread isn’t part of a workgroup.

## See Also

### Properties
- [reserved](./reserved.md)
  System-specific information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitrendercontext/workgroup)*