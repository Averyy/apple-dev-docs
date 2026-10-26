# BAManagedErrorCodeLocalAvailabilityFailure

**Framework**: Background Assets  
**Kind**: case  
**Role**: Enumeration Case

An error code that indicates that the system couldn’t ensure the local availability of some or all of the requested asset packs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
BAManagedErrorCodeLocalAvailabilityFailure
```

#### Discussion

Refer to the values in `-[NSError userInfo]` for the keys [`BASuccessesErrorKey`](../basuccesseserrorkey.md) and [`BAFailuresErrorKey`](../bafailureserrorkey.md) for, respectively, the asset packs the local availability of which the system ensured successfully and the asset packs the local availability of which the system couldn’t ensure with associated underlying errors for the latter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/bamanagederrorcode/bamanagederrorcodelocalavailabilityfailure)*