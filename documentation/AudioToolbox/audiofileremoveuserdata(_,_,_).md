# AudioFileRemoveUserData(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Removes a user data item from an audio file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileRemoveUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32) -> OSStatus
```

```c
extern OSStatus AudioFileRemoveUserData(AudioFileID inAudioFile, UInt32 inUserDataID, UInt32 inIndex);
```

#### Return Value

A result code if there’s an error (see Result Codes) or `noErr` if the operation succeeds.

## Parameters

- `inAudioFile`: The audio file that contains the user data item you want to remove.
- `inUserDataID`: The four-character code such as `COMM` of the user data item.
- `inIndex`: An index specifying the chunk to remove. Use this parameter if the file contains more than one user data item with the four-character code that you specified in the `inUserDataID` parameter.

## See Also

### Working with User Data
- [func AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecountuserdata%28_,_,_%29.md)
  Gets the number of user data items with a specified ID in a file.
- [func AudioFileGetUserDataSize(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilegetuserdatasize%28_,_,_,_%29.md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserDataSize64(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](./audiofilegetuserdatasize64%28_,_,_,_%29.md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserData(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilegetuserdata%28_,_,_,_,_%29.md)
  Gets a chunk from an audio file.
- [func AudioFileGetUserDataAtOffset(AudioFileID, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilegetuserdataatoffset%28_,_,_,_,_,_%29.md)
  Gets part of the data from a chunk in an audio file.
- [func AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilesetuserdata%28_,_,_,_,_%29.md)
  Sets a user data item in an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileremoveuserdata(_:_:_:))*