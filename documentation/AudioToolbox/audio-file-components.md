# Audio File Components

**Framework**: Audio Toolbox

Get information about audio file formats, and about files containing audio data.

## Topics

### Opening and Closing Audio Files
- [func AudioFileComponentCreateURL(AudioFileComponent, CFURL, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](audiofilecomponentcreateurl(_:_:_:_:).md)
- [func AudioFileComponentOpenURL(AudioFileComponent, CFURL, Int8, Int32) -> OSStatus](audiofilecomponentopenurl(_:_:_:_:).md)
- [func AudioFileComponentOpenWithCallbacks(AudioFileComponent, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc) -> OSStatus](audiofilecomponentopenwithcallbacks(_:_:_:_:_:_:).md)
- [func AudioFileComponentCloseFile(AudioFileComponent) -> OSStatus](audiofilecomponentclosefile(_:).md)
- [func AudioFileComponentOptimize(AudioFileComponent) -> OSStatus](audiofilecomponentoptimize(_:).md)
- [typealias AudioFileComponent](audiofilecomponent.md)
- [typealias AudioFileComponentPropertyID](audiofilecomponentpropertyid.md)
- [typealias AudioFileComponentCreateURLProc](audiofilecomponentcreateurlproc.md)
- [typealias AudioFileComponentOpenWithCallbacksProc](audiofilecomponentopenwithcallbacksproc.md)
- [typealias AudioFileComponentOpenURLProc](audiofilecomponentopenurlproc.md)
- [typealias AudioFileComponentCloseProc](audiofilecomponentcloseproc.md)
- [typealias AudioFileComponentOptimizeProc](audiofilecomponentoptimizeproc.md)
### Configuring the Callbacks
- [func AudioFileComponentInitializeWithCallbacks(AudioFileComponent, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc, UInt32, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](audiofilecomponentinitializewithcallbacks(_:_:_:_:_:_:_:_:_:).md)
- [Audio File Component Selectors](1404047-audio-file-component-selectors.md)
- [typealias AudioFileComponentInitializeWithCallbacksProc](audiofilecomponentinitializewithcallbacksproc.md)
### Getting the Global Information
- [func AudioFileComponentGetGlobalInfo(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetglobalinfo(_:_:_:_:_:_:).md)
- [func AudioFileComponentGetGlobalInfoSize(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentgetglobalinfosize(_:_:_:_:_:).md)
- [typealias AudioFileComponentGetGlobalInfoProc](audiofilecomponentgetglobalinfoproc.md)
- [typealias AudioFileComponentGetGlobalInfoSizeProc](audiofilecomponentgetglobalinfosizeproc.md)
### Accessing the User Data
- [func AudioFileComponentGetUserData(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetuserdata(_:_:_:_:_:).md)
- [func AudioFileComponentSetUserData(AudioFileComponent, UInt32, UInt32, UInt32, UnsafeRawPointer) -> OSStatus](audiofilecomponentsetuserdata(_:_:_:_:_:).md)
- [func AudioFileComponentCountUserData(AudioFileComponent, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentcountuserdata(_:_:_:).md)
- [func AudioFileComponentGetUserDataSize(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentgetuserdatasize(_:_:_:_:).md)
- [func AudioFileComponentRemoveUserData(AudioFileComponent, UInt32, UInt32) -> OSStatus](audiofilecomponentremoveuserdata(_:_:_:).md)
- [typealias AudioFileComponentCountUserDataProc](audiofilecomponentcountuserdataproc.md)
- [typealias AudioFileComponentGetUserDataProc](audiofilecomponentgetuserdataproc.md)
- [typealias AudioFileComponentGetUserDataSizeProc](audiofilecomponentgetuserdatasizeproc.md)
- [typealias AudioFileComponentRemoveUserDataProc](audiofilecomponentremoveuserdataproc.md)
- [typealias AudioFileComponentSetUserDataProc](audiofilecomponentsetuserdataproc.md)
- [typealias CountUserDataFDF](countuserdatafdf.md)
- [typealias GetUserDataFDF](getuserdatafdf.md)
- [typealias GetUserDataSizeFDF](getuserdatasizefdf.md)
### Accessing Properties
- [func AudioFileComponentGetProperty(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetproperty(_:_:_:_:).md)
- [func AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](audiofilecomponentgetpropertyinfo(_:_:_:_:).md)
- [func AudioFileComponentSetProperty(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilecomponentsetproperty(_:_:_:_:).md)
- [typealias AudioFileComponentGetPropertyInfoProc](audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentGetPropertyProc](audiofilecomponentgetpropertyproc.md)
- [typealias AudioFileComponentSetPropertyProc](audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](1404186-audio-file-component-specific-pr.md)
### Reading and Writing Data
- [func AudioFileComponentReadBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadbytes(_:_:_:_:_:).md)
- [func AudioFileComponentReadPacketData(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadpacketdata(_:_:_:_:_:_:_:).md)
- [func AudioFileComponentReadPackets(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadpackets(_:_:_:_:_:_:_:).md)
- [func AudioFileComponentWriteBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilecomponentwritebytes(_:_:_:_:_:).md)
- [func AudioFileComponentWritePackets(AudioFileComponent, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilecomponentwritepackets(_:_:_:_:_:_:_:).md)
- [typealias AudioFileComponentReadBytesProc](audiofilecomponentreadbytesproc.md)
- [typealias AudioFileComponentReadPacketDataProc](audiofilecomponentreadpacketdataproc.md)
- [typealias AudioFileComponentReadPacketsProc](audiofilecomponentreadpacketsproc.md)
- [typealias AudioFileComponentWriteBytesProc](audiofilecomponentwritebytesproc.md)
- [typealias AudioFileComponentWritePacketsProc](audiofilecomponentwritepacketsproc.md)
### Checking the File Format
- [func AudioFileComponentFileDataIsThisFormat(AudioFileComponent, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentfiledataisthisformat(_:_:_:_:).md)
- [func AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentextensionisthisformat(_:_:_:).md)
- [typealias AudioFileComponentExtensionIsThisFormatProc](audiofilecomponentextensionisthisformatproc.md)
- [typealias AudioFileComponentFileDataIsThisFormatProc](audiofilecomponentfiledataisthisformatproc.md)
- [typealias GetPropertyFDF](getpropertyfdf.md)
- [typealias GetPropertyInfoFDF](getpropertyinfofdf.md)

## See Also

- [Audio Format Services](audio-format-services.md)
  Access information about audio formats and codecs.
- [Audio File Services](audio-file-services.md)
  Read or write a variety of audio data to or from disk or a memory buffer.
- [Extended Audio File Services](extended-audio-file-services.md)
  Read and write compressed files and linear PCM audio files using a simplified interface.
- [Audio File Stream Services](audio-file-stream-services.md)
  Parse streamed audio files as the data arrives on the user’s computer.
- [Core Audio File Format](core-audio-file-format.md)
  Parse the structure of Core Audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-file-components)*