# componentName

**Framework**: Audio Toolbox  
**Kind**: property

The audio unit’s component’s name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var componentName: String? { get }
```

#### Discussion

By convention, an audio unit’s component name is “[`manufacturerName`](auaudiounit/manufacturername.md): [`audioUnitName`](auaudiounit/audiounitname.md)”.

## See Also

- [var componentDescription: AudioComponentDescription](auaudiounit/componentdescription.md)
  The component description with which the audio unit was created.
- [var component: AudioComponent](auaudiounit/component.md)
  The component found in the component description with which the audio unit was created.
- [var componentVersion: UInt32](auaudiounit/componentversion.md)
  The audio unit’s component’s version.
- [var audioUnitName: String?](auaudiounit/audiounitname.md)
  The audio unit’s name, derived from the component’s name.
- [var audioUnitShortName: String?](auaudiounit/audiounitshortname.md)
- [var manufacturerName: String?](auaudiounit/manufacturername.md)
  The manufacturer’s name, derived from the component’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/componentname)*