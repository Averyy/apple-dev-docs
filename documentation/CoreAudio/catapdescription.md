# CATapDescription

**Framework**: Core Audio  
**Kind**: class  
**Role**: Class

This class describes a tap object that contains an input stream.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class CATapDescription
```

```objc
@interface CATapDescription : NSObject
```

#### Overview

The input stream is a mix of all of the specified processes’ output audio.

## Topics

### Initializers
- [init()](./catapdescription/init%28%29.md)
- [convenience init(excludingProcesses: [AudioObjectID], deviceUID: String, stream: UInt)](./catapdescription/init%28excludingprocesses,deviceuid,stream%29.md)
- [convenience init(monoGlobalTapButExcludeProcesses: [AudioObjectID])](./catapdescription/init%28monoglobaltapbutexcludeprocesses%29.md)
- [convenience init(monoMixdownOfProcesses: [AudioObjectID])](./catapdescription/init%28monomixdownofprocesses%29.md)
- [convenience init(processes: [AudioObjectID], deviceUID: String, stream: UInt)](./catapdescription/init%28processes,deviceuid,stream%29.md)
- [convenience init(stereoGlobalTapButExcludeProcesses: [AudioObjectID])](./catapdescription/init%28stereoglobaltapbutexcludeprocesses%29.md)
- [convenience init(stereoMixdownOfProcesses: [AudioObjectID])](./catapdescription/init%28stereomixdownofprocesses%29.md)
### Instance Properties
- [var bundleIDs: [String]](./catapdescription/bundleids.md)
- [var deviceUID: String?](./catapdescription/deviceuid.md)
- [var isExclusive: Bool](./catapdescription/isexclusive.md)
- [var isMixdown: Bool](./catapdescription/ismixdown.md)
- [var isMono: Bool](./catapdescription/ismono.md)
- [var isPrivate: Bool](./catapdescription/isprivate.md)
- [var isProcessRestoreEnabled: Bool](./catapdescription/isprocessrestoreenabled.md)
- [var muteBehavior: CATapMuteBehavior](./catapdescription/mutebehavior.md)
- [var name: String](./catapdescription/name.md)
- [var processes: [AudioObjectID]](./catapdescription/processes-1m4cr.md)
- [var stream: UInt?](./catapdescription/stream-ajk3.md)
- [var uuid: UUID](./catapdescription/uuid.md)
- [processes](./catapdescription/processes-3cdzw.md)
- [stream](./catapdescription/stream-u4ff.md)
### Instance Methods
- [- initExcludingProcesses:andDeviceUID:withStream:](./catapdescription/initexcludingprocesses_anddeviceuid_withstream_.md)
- [- initMonoGlobalTapButExcludeProcesses:](./catapdescription/initmonoglobaltapbutexcludeprocesses_.md)
- [- initMonoMixdownOfProcesses:](./catapdescription/initmonomixdownofprocesses_.md)
- [- initStereoGlobalTapButExcludeProcesses:](./catapdescription/initstereoglobaltapbutexcludeprocesses_.md)
- [- initStereoMixdownOfProcesses:](./catapdescription/initstereomixdownofprocesses_.md)
- [- initWithProcesses:andDeviceUID:withStream:](./catapdescription/initwithprocesses_anddeviceuid_withstream_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription)*