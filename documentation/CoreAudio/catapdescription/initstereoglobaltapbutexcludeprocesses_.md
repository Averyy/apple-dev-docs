# initStereoGlobalTapButExcludeProcesses:

**Framework**: Core Audio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```objc
- (instancetype) initStereoGlobalTapButExcludeProcesses:(NSArray<NSNumber *> *) processesObjectIDsToExcludeFromTap;
```

## Discussion

Mix all processes to a stereo stream except the given processes.  Mono sources will be duplicated in both right and left channels.

## Parameters

- `processesObjectIDsToExcludeFromTap`: An NSArray of NSNumbers where each NSNumber holds an AudioObjectID of the process object to exclude from the tap. All other processes that output audio will be included in the tap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/catapdescription/initstereoglobaltapbutexcludeprocesses:)*