# kAudioFormatProperty_HardwareCodecCapabilities

**Framework**: Audio Toolbox  
**Kind**: var

A `UInt32` value indicating the number of codecs from the specified list that can be used, if the application were to begin using them in the specified order. Set the `inSpecifier` parameter to an array of `AudioClassDescription` structures that describes a set of one or more audio codecs. If the property value is the same as the size of the array in the `inSpecifier` parameter, all of the specified codecs can be used.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioFormatProperty_HardwareCodecCapabilities: AudioFormatPropertyID { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_hardwarecodeccapabilities)*