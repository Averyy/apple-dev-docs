# headphoneSafetyAudioLevel

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * headphoneSafetyAudioLevel;
```

#### Discussion

Reduce Loud Audio

iPhone can analyze headphone audio and reduce any sound that is over a set decibel level. A nil value means the setting is disabled. If the setting is enabled, the property will hold the decibel value that headphone audio sound volume is not to exceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/sracousticsettings/headphonesafetyaudiolevel-9ziqo)*