# init(excludingProcesses:deviceUID:stream:)

**Framework**: Core Audio  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 14.0+

## Declaration

```swift
convenience init(excludingProcesses processesIDsToExcludeFromTap: [AudioObjectID], deviceUID: String, stream: UInt)
```

## See Also

### Initializers
- [init()](./init%28%29.md)
- [convenience init(monoGlobalTapButExcludeProcesses: [AudioObjectID])](./init%28monoglobaltapbutexcludeprocesses%29.md)
- [convenience init(monoMixdownOfProcesses: [AudioObjectID])](./init%28monomixdownofprocesses%29.md)
- [convenience init(processes: [AudioObjectID], deviceUID: String, stream: UInt)](./init%28processes,deviceuid,stream%29.md)
- [convenience init(stereoGlobalTapButExcludeProcesses: [AudioObjectID])](./init%28stereoglobaltapbutexcludeprocesses%29.md)
- [convenience init(stereoMixdownOfProcesses: [AudioObjectID])](./init%28stereomixdownofprocesses%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription/init(excludingprocesses:deviceuid:stream:))*