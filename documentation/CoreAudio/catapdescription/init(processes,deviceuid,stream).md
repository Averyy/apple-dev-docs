# init(processes:deviceUID:stream:)

**Framework**: Core Audio  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 14.0+

## Declaration

```swift
convenience init(processes processesIDsToIncludeInTap: [AudioObjectID], deviceUID: String, stream: UInt)
```

## See Also

### Initializers
- [init()](./init%28%29.md)
- [convenience init(excludingProcesses: [AudioObjectID], deviceUID: String, stream: UInt)](./init%28excludingprocesses,deviceuid,stream%29.md)
- [convenience init(monoGlobalTapButExcludeProcesses: [AudioObjectID])](./init%28monoglobaltapbutexcludeprocesses%29.md)
- [convenience init(monoMixdownOfProcesses: [AudioObjectID])](./init%28monomixdownofprocesses%29.md)
- [convenience init(stereoGlobalTapButExcludeProcesses: [AudioObjectID])](./init%28stereoglobaltapbutexcludeprocesses%29.md)
- [convenience init(stereoMixdownOfProcesses: [AudioObjectID])](./init%28stereomixdownofprocesses%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription/init(processes:deviceuid:stream:))*