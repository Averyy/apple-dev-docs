# ExtAudioFileOpen

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Deprecated. Use the [`ExtAudioFileOpenURL(_:_:)`](./extaudiofileopenurl%28_,_%29.md) function instead.

**Availability**:
- macOS 10.4+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus ExtAudioFileOpen(const struct FSRef *inFSRef, ExtAudioFileRef*outExtAudioFile);
```

#### Return Value

A result code.

#### Discussion

Allocates a new ExtAudioFileRef for reading an existing audio file.

##### Special Considerations

This function is deprecated. Use the [`ExtAudioFileOpenURL(_:_:)`](./extaudiofileopenurl%28_,_%29.md) function instead.

## Parameters

- `inFSRef`: The audio file to read.
- `outExtAudioFile`: On exit, a newly allocated ExtAudioAudioFileRef.

## See Also

### Deprecated Functions
- [ExtAudioFileCreateNew](./extaudiofilecreatenew.md)
  Deprecated. Use the [`ExtAudioFileCreateWithURL(_:_:_:_:_:_:)`](./extaudiofilecreatewithurl%28_,_,_,_,_,_%29.md) function instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofileopen)*