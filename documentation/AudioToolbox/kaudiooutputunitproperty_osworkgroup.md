# kAudioOutputUnitProperty_OSWorkgroup

**Framework**: Audio Toolbox  
**Kind**: case  
**Role**: Enumeration Case

The workgroup associated with the audio device underlying this Audio Unit.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```c
kAudioOutputUnitProperty_OSWorkgroup
```

## Mentions

- [Adding Parallel Real-Time Threads to Audio Workgroups](./adding-parallel-real-time-threads-to-audio-workgroups.md)

#### Discussion

The value of this key is an [`os_workgroup_t`](../os/os_workgroup_t.md) object.

Workgroups allow multiple threads to coordinate their activities for realtime operations. For Audio Units, this coordination occurs between the Audio Unit and other processes, such as the audio server and host app. The system uses the workgroup to observe the threads’ CPU usage and dynamically balance the competing considerations of power consumption and real-time rendering capacity.

This version 2 property is bridged to the version 3 [`osWorkgroup`](./auaudiounit/osworkgroup.md) property of [`AUAudioUnit`](./auaudiounit.md).

## See Also

### Device Workgroup
- [var kAudioDevicePropertyIOThreadOSWorkgroup: AudioObjectPropertySelector](../CoreAudio/kaudiodevicepropertyiothreadosworkgroup.md)
  The device’s workgroup object, which you use to coordinate your threads with the threads of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiooutputunitproperty_osworkgroup)*