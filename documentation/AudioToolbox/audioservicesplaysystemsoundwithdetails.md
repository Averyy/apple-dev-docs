# AudioServicesPlaySystemSoundWithDetails

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- visionOS 26.0+

## Declaration

```c
extern void AudioServicesPlaySystemSoundWithDetails(SystemSoundID inSystemSoundID, CFDictionaryRef inDetails, void (^inCompletionBlock)());
```

#### Discussion

Play the sound designated by the provided SystemSoundID.

## Parameters

- `inSystemSoundID`: A SystemSoundID for the system sound server to play.
- `inDetails`: A set of details as described above.
- `inCompletionBlock`: The completion block gets executed for every attempt to play a system sound irrespective of success or failure. The callbacks are issued on a serial queue and the client is responsible for handling thread safety.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesplaysystemsoundwithdetails)*