# ExtAudioFileCreateNew

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Deprecated. Use the [`ExtAudioFileCreateWithURL(_:_:_:_:_:_:)`](./extaudiofilecreatewithurl%28_,_,_,_,_,_%29.md) function instead.

**Availability**:
- macOS 10.4+ - Deprecated in 10.6

## Declaration

```c
extern OSStatus ExtAudioFileCreateNew(const struct FSRef *inParentDir, CFStringRef inFileName, AudioFileTypeID inFileType, const AudioStreamBasicDescription *inStreamDesc, const AudioChannelLayout *inChannelLayout, ExtAudioFileRef*outExtAudioFile);
```

## Return Value

A result code.

## Discussion

Creates a new audio file.

If the file to be created is in a compressed format, it is permissible for the sample rate in inStreamDesc to be 0, since in all cases, the file’s encoding AudioConverter may produce audio at a different sample rate than the source. The file will be created with the audio format actually produced by the encoder.

### Special Considerations

This function is deprecated. Use the [`ExtAudioFileCreateWithURL(_:_:_:_:_:_:)`](./extaudiofilecreatewithurl%28_,_,_,_,_,_%29.md) function instead.

## Parameters

- `inParentDir`: The directory in which to create the new file.
- `inFileName`: The name of the new file.
- `inFileType`: The type of file to create. This is a constant from AudioToolbox/AudioFile.h, e.g. kAudioFileAIFFType. Note that this is not an HFSTypeCode.
- `inStreamDesc`: The format of the audio data to be written to the file.
- `inChannelLayout`: The channel layout of the audio data. If non-null, this must be consistent with the number of channels specified by inStreamDesc.
- `outExtAudioFile`: On output, a newly allocated extended audio file object.

## See Also

### Deprecated Functions
- [ExtAudioFileOpen](./extaudiofileopen.md)
  Deprecated. Use the [`ExtAudioFileOpenURL(_:_:)`](./extaudiofileopenurl%28_,_%29.md) function instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/extaudiofilecreatenew)*