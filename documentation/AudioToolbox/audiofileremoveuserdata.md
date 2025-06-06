# AudioFileRemoveUserData(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

#### Return Value

A result code if there’s an error (see Result Codes) or `noErr` if the operation succeeds.

## Parameters

- `inAudioFile`: The audio file that contains the user data item you want to remove.
- `inUserDataID`: The four-character code such as   of the user data item.
- `inIndex`: An index specifying the chunk to remove. Use this parameter if the file contains more than one user data item with the four-character code that you specified in the   parameter.

## See Also

- [func AudioFileCountUserData(AudioFileID, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecountuserdata(_:_:_:).md)
  Gets the number of user data items with a specified ID in a file.
- [func AudioFileGetUserDataSize(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilegetuserdatasize(_:_:_:_:).md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserDataSize64(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](audiofilegetuserdatasize64(_:_:_:_:).md)
  Gets the size of a user data item in an audio file.
- [func AudioFileGetUserData(AudioFileID, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetuserdata(_:_:_:_:_:).md)
  Gets a chunk from an audio file.
- [func AudioFileGetUserDataAtOffset(AudioFileID, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilegetuserdataatoffset(_:_:_:_:_:_:).md)
  Gets part of the data from a chunk in an audio file.
- [func AudioFileSetUserData(AudioFileID, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](audiofilesetuserdata(_:_:_:_:_:).md)
  Sets a user data item in an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileremoveuserdata(_:_:_:))*