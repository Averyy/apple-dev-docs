# AudioServerPlugInRegisterMediaDeviceExtension

**Framework**: Core Audio  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```c
extern OSStatus AudioServerPlugInRegisterMediaDeviceExtension(AudioServerPlugInDriverRef inPlugIn, void (^interruptionHandler)());
```

## Return Value

An OSStatus indicating success or failure.

## Discussion

This is used to register an AudioServerPlugin interface to host a driver for a remote media device to be used in conjunction with [Creating a media device extension](../MediaDevice/creating-a-media-device-extension.md).

AudioServerPlugIns that are registered this way are restricted to presenting a single output audio device, which must have a transport type of [`kAudioDeviceTransportTypeRemoteScreen`](./kaudiodevicetransporttyperemotescreen.md) or [`kAudioDeviceTransportTypeRemoteStreaming`](./kaudiodevicetransporttyperemotestreaming.md). If these conditions are not met, the registration will fail with a result of [`kAudioHardwareIllegalOperationError`](./kaudiohardwareillegaloperationerror.md). It is also expected that the device UID ([`kAudioDevicePropertyDeviceUID`](./kaudiodevicepropertydeviceuid.md)) matches the [`MediaOutputDevice`](../MediaDevice/mediaoutputdevice.md)’s [`id`](../MediaDevice/mediaoutputdevice/id.md).

## Parameters

- `inPlugIn`: The plug-in interface that will be called by the system.
- `interruptionHandler`: The handler that will be called when the connection to the audio server is interrupted


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverpluginregistermediadeviceextension)*