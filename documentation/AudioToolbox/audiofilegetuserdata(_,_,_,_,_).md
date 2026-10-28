# AudioFileGetUserData(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets a chunk from an audio file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileGetUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileGetUserData(AudioFileID inAudioFile, UInt32 inUserDataID, UInt32 inIndex, UInt32 *ioUserDataSize, void *outUserData);
```

## Return Value

A result code if there’s an error (see Result Codes) or `noErr` if the operation succeeds.

## Parameters

- `inAudioFile`: The audio file whose chunk you want to get.
- `inUserDataID`: The four-character code of the designated chunk.
- `inIndex`: An index that specifies which chunk with the four-character code specified in the `inUserDataID` parameter you want to query.
- `ioUserDataSize`: On input, a pointer to the size of the buffer that contains the designated chunk. On output, a pointer to the size of bytes that the system copied to the buffer.
- `outUserData`: A pointer to a buffer in which to copy the chunk data.

## See Also

### Working with User Data
- [func AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecountuserdata%28_,_,_%29.md)
  Gets the number of user data items with a specified ID in a file.
- [func AudioFileGetUserDataSize(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilegetuserdatasize%28_,_,_,_%29.md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserDataSize64(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](./audiofilegetuserdatasize64%28_,_,_,_%29.md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserDataAtOffset(AudioFileID, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilegetuserdataatoffset%28_,_,_,_,_,_%29.md)
  Gets part of the data from a chunk in an audio file.
- [func AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilesetuserdata%28_,_,_,_,_%29.md)
  Sets a user data item in an audio file.
- [func AudioFileRemoveUserData(AudioFileID, UInt32, UInt32) -> OSStatus](./audiofileremoveuserdata%28_,_,_%29.md)
  Removes a user data item from an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilegetuserdata(_:_:_:_:_:))*