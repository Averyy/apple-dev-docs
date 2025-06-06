# AudioFileGetUserDataSize(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets the size of a user data item in an audio file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileGetUserDataSize(_ inAudioFile: AudioFileID, _ inUserDataID: UInt32, _ inIndex: UInt32, _ outUserDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus
```

#### Return Value

A result code if there’s an error (see Result Codes) or `noErr` if the operation succeeds.

#### Discussion

In this function,  refers to:

- Chunks in AIFF, CAF, and WAVE files
- Resources in Sound Designer II files
- Other types of information in other files

## Parameters

- `inAudioFile`: The audio file whose user data item size you want.
- `inUserDataID`: The four-character code of the designated user data item.
- `inIndex`: An index of the user data item with the four-character code specified in   that you want to query.
- `outUserDataSize`: On output, if successful, the size of the user data item.

## See Also

- [func AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecountuserdata(_:_:_:).md)
  Gets the number of user data items with a specified ID in a file.
- [func AudioFileGetUserDataSize64(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](audiofilegetuserdatasize64(_:_:_:_:).md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserData(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetuserdata(_:_:_:_:_:).md)
  Gets a chunk from an audio file.
- [func AudioFileGetUserDataAtOffset(AudioFileID, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetuserdataatoffset(_:_:_:_:_:_:).md)
  Gets part of the data from a chunk in an audio file.
- [func AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetuserdata(_:_:_:_:_:).md)
  Sets a user data item in an audio file.
- [func AudioFileRemoveUserData(AudioFileID, UInt32, UInt32) -> OSStatus](audiofileremoveuserdata(_:_:_:).md)
  Removes a user data item from an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilegetuserdatasize(_:_:_:_:))*