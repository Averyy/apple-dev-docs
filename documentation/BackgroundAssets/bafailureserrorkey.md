# BAFailuresErrorKey

**Framework**: Background Assets  
**Kind**: var  
**Role**: Global Variable

The `-[NSError userInfo]` key for the set of asset packs the local availability of which the system couldn’t ensure and their respective associated underlying errors.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```c
extern NSErrorUserInfoKey const BAFailuresErrorKey;
```

#### Discussion

This key is relevant when the error code is [`BAManagedErrorCodeLocalAvailabilityFailure`](./bamanagederrorcode/bamanagederrorcodelocalavailabilityfailure.md). Its value should be an `NSDictionary<BAAssetPack*, NSError*>` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bafailureserrorkey)*