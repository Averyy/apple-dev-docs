# AVAudioEnvironmentNode

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that simulates a 3D audio environment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioEnvironmentNode
```

```objc
@interface AVAudioEnvironmentNode : AVAudioNode
```

## Overview

The `AVAudioEnvironmentNode` class is a mixer node that simulates a 3D audio environment. Any node that conforms to [`AVAudioMixing`](./avaudiomixing.md) can act as a source node, such as [`AVAudioPlayerNode`](./avaudioplayernode.md).

The environment node has an implicit listener. You set the listener’s position and orientation, and the system then controls the way the user experiences the virtual world.

To help characterize the environment, this class defines properties for distance attenuation and reverberation.

[`AVAudio3DMixingSourceMode`](./avaudio3dmixingsourcemode.md) affects how inputs with different channel configurations render. Spatialization applies only to inputs with a mono channel connection format. This class doesn’t spatialize stereo inputs or support inputs with connection formats of more than two channels.

To set the node’s output to a multichannel format, use an [`AVAudioFormat`](./avaudioformat.md) that has one of the following [Audio Channel Layout Tags](../CoreAudioTypes/audio-channel-layout-tags.md):

- [`kAudioChannelLayoutTag_AudioUnit_4`](../CoreAudioTypes/kaudiochannellayouttag_audiounit_4.md)
- [`kAudioChannelLayoutTag_AudioUnit_5_0`](../CoreAudioTypes/kaudiochannellayouttag_audiounit_5_0.md)
- [`kAudioChannelLayoutTag_AudioUnit_6_0`](../CoreAudioTypes/kaudiochannellayouttag_audiounit_6_0.md)
- [`kAudioChannelLayoutTag_AudioUnit_7_0`](../CoreAudioTypes/kaudiochannellayouttag_audiounit_7_0.md)
- [`kAudioChannelLayoutTag_AudioUnit_7_0_Front`](../CoreAudioTypes/kaudiochannellayouttag_audiounit_7_0_front.md)
- [`kAudioChannelLayoutTag_AudioUnit_8`](../CoreAudioTypes/kaudiochannellayouttag_audiounit_8.md)

## Topics

### Creating an environment node
- [init()](./avaudioenvironmentnode/init%28%29.md)
  Creates a new environment node object.
### Positioning the listener
- [var listenerPosition: AVAudio3DPoint](./avaudioenvironmentnode/listenerposition.md)
  The listener’s position in the 3D environment.
- [var listenerAngularOrientation: AVAudio3DAngularOrientation](./avaudioenvironmentnode/listenerangularorientation.md)
  The listener’s angular orientation in the environment.
- [var listenerVectorOrientation: AVAudio3DVectorOrientation](./avaudioenvironmentnode/listenervectororientation.md)
  The listener’s vector orientation in the environment.
- [var isListenerHeadTrackingEnabled: Bool](./avaudioenvironmentnode/islistenerheadtrackingenabled.md)
  A Boolean value that indicates whether the listener orientation is automatically rotated based on head orientation.
### Configuring attenuation and reverb
- [var distanceAttenuationParameters: AVAudioEnvironmentDistanceAttenuationParameters](./avaudioenvironmentnode/distanceattenuationparameters.md)
  The distance attenuation parameters for the environment.
- [var reverbParameters: AVAudioEnvironmentReverbParameters](./avaudioenvironmentnode/reverbparameters.md)
  The reverb parameters for the environment.
### Configuring the output
- [var outputVolume: Float](./avaudioenvironmentnode/outputvolume.md)
  The mixer’s output volume.
- [var outputType: AVAudioEnvironmentOutputType](./avaudioenvironmentnode/outputtype.md)
  The type of output hardware.
- [enum AVAudioEnvironmentOutputType](./avaudioenvironmentoutputtype.md)
  The output types for using with the automatic 3D mixing rendering algorithm.
### Inspecting rendering algorithms
- [var applicableRenderingAlgorithms: [NSNumber]](./avaudioenvironmentnode/applicablerenderingalgorithms.md)
  An array of rendering algorithms applicable to the environment node.
### Getting the input bus
- [var nextAvailableInputBus: AVAudioNodeBus](./avaudioenvironmentnode/nextavailableinputbus.md)
  An unused input bus.

## Relationships

### Inherits From
- [AVAudioNode](./avaudionode.md)
### Conforms To
- [AVAudio3DMixing](./avaudio3dmixing.md)
- [AVAudioMixing](./avaudiomixing.md)
- [AVAudioStereoMixing](./avaudiostereomixing.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Spatial audio
- [class AVAudioEnvironmentDistanceAttenuationParameters](./avaudioenvironmentdistanceattenuationparameters.md)
  An object that specifies the amount of attenuation distance, the gradual loss in audio intensity, and other characteristics.
- [class AVAudioEnvironmentReverbParameters](./avaudioenvironmentreverbparameters.md)
  A class that encapsulates the parameters that you use to control the reverb of the environment node class.
- [protocol AVAudio3DMixing](./avaudio3dmixing.md)
  A collection of properties that define 3D mixing properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode)*