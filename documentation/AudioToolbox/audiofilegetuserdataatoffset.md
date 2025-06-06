# AudioFileGetUserDataAtOffset(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets part of the data from a chunk in an audio file.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileGetUserDataAtOffset(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inOffset: Int64, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

A result code if there’s an error (see Result Codes) or `noErr` if the operation succeeds.

#### Discussion

See [`AudioFileGetUserDataSize64(_:_:_:_:)`](audiofilegetuserdatasize64(_:_:_:_:).md) for an example of using this function to parse the Audio Definition Model (ADM) of a BW64 file, which is 64-bit and based on WAVE.

## Parameters

- `inAudioFile`: The audio file whose chunk you want to get data from.
- `inUserDataID`: The four-character code of the designated chunk.
- `inIndex`: An index that specifies which chunk with the four-character code specified in the   parameter you want to query.
- `inOffset`: An offset from the first byte of the chunk to the first byte to get.
- `ioUserDataSize`: On input, a pointer to the size of the buffer that contains the designated chunk. On output, a pointer to the size of bytes that the system copied to the buffer.
- `outUserData`: A pointer to a buffer in which to copy the chunk data.

## See Also

- [func AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecountuserdata(_:_:_:).md)
  Gets the number of user data items with a specified ID in a file.
- [func AudioFileGetUserDataSize(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilegetuserdatasize(_:_:_:_:).md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserDataSize64(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](audiofilegetuserdatasize64(_:_:_:_:).md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserData(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetuserdata(_:_:_:_:_:).md)
  Gets a chunk from an audio file.
- [func AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetuserdata(_:_:_:_:_:).md)
  Sets a user data item in an audio file.
- [func AudioFileRemoveUserData(AudioFileID, UInt32, UInt32) -> OSStatus](audiofileremoveuserdata(_:_:_:).md)
  Removes a user data item from an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilegetuserdataatoffset(_:_:_:_:_:_:))*