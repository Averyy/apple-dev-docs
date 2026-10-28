# AudioFileCountUserData(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets the number of user data items with a specified ID in a file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileCountUserData(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ outNumberItems: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioFileCountUserData(AudioFileID inAudioFile, UInt32 inUserDataID, UInt32 *outNumberItems);
```

## Return Value

A result code if there’s an error (see Result Codes) or `noErr` if the operation succeeds.

## Discussion

In this function, *user data* refers to:

- Chunks in AIFF, CAF, and WAVE files
- Resources in Sound Designer II files
- Other types of information in other files

## Parameters

- `inAudioFile`: The audio file whose user data items are to be counted.
- `inUserDataID`: The four-character code (such as `COMM`) of the user data item.
- `outNumberItems`: On output, a pointer to the number of user data items of this type in the file.

## See Also

### Working with User Data
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
- [func AudioFileRemoveUserData(AudioFileID, UInt32, UInt32) -> OSStatus](./audiofileremoveuserdata%28_,_,_%29.md)
  Removes a user data item from an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecountuserdata(_:_:_:))*