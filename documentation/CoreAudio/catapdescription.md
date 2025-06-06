# CATapDescription

**Framework**: Core Audio  
**Kind**: class

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class CATapDescription
```

## Topics

### Initializers
- [init()](catapdescription/init.md)
- [convenience init(excludingProcesses: [AudioObjectID], deviceUID: String, stream: UInt)](catapdescription/init(excludingprocesses:deviceuid:stream:).md)
- [convenience init(monoGlobalTapButExcludeProcesses: [AudioObjectID])](catapdescription/init(monoglobaltapbutexcludeprocesses:).md)
- [convenience init(monoMixdownOfProcesses: [AudioObjectID])](catapdescription/init(monomixdownofprocesses:).md)
- [convenience init(processes: [AudioObjectID], deviceUID: String, stream: UInt)](catapdescription/init(processes:deviceuid:stream:).md)
- [convenience init(stereoGlobalTapButExcludeProcesses: [AudioObjectID])](catapdescription/init(stereoglobaltapbutexcludeprocesses:).md)
- [convenience init(stereoMixdownOfProcesses: [AudioObjectID])](catapdescription/init(stereomixdownofprocesses:).md)
### Instance Properties
- [var deviceUID: String?](catapdescription/deviceuid.md)
- [var isExclusive: Bool](catapdescription/isexclusive.md)
- [var isMixdown: Bool](catapdescription/ismixdown.md)
- [var isMono: Bool](catapdescription/ismono.md)
- [var isPrivate: Bool](catapdescription/isprivate.md)
- [var muteBehavior: CATapMuteBehavior](catapdescription/mutebehavior.md)
- [var name: String](catapdescription/name.md)
- [var processes: [AudioObjectID]](catapdescription/processes-1m4cr.md)
- [var stream: UInt?](catapdescription/stream-ajk3.md)
- [var uuid: UUID](catapdescription/uuid.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription)*