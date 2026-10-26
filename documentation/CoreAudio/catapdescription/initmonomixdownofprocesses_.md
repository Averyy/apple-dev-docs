# initMonoMixdownOfProcesses:

**Framework**: Core Audio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```objc
- (instancetype) initMonoMixdownOfProcesses:(NSArray<NSNumber *> *) processesObjectIDsToIncludeInTap;
```

#### Discussion

Mix all given process audio streams audio to mono.

## Parameters

- `processesObjectIDsToIncludeInTap`: An NSArray of NSNumbers where each NSNumber holds an AudioObjectID of the process object to include in the tap


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription/initmonomixdownofprocesses:)*