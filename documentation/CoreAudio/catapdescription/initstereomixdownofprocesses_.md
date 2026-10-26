# initStereoMixdownOfProcesses:

**Framework**: Core Audio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```objc
- (instancetype) initStereoMixdownOfProcesses:(NSArray<NSNumber *> *) processesObjectIDsToIncludeInTap;
```

#### Discussion

Mix all given process audio streams down to stereo.  Mono sources will be duplicated in both right and left channels.

## Parameters

- `processesObjectIDsToIncludeInTap`: An NSArray of NSNumbers where each NSNumber holds an AudioObjectID of the process object to include in the tap


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription/initstereomixdownofprocesses:)*