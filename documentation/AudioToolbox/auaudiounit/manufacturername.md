# manufacturerName

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The manufacturer’s name, derived from the component’s name.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var manufacturerName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * manufacturerName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * manufacturerName;
```

## See Also

### Describing the Audio Unit
- [var componentDescription: AudioComponentDescription](./componentdescription.md)
  The component description with which the audio unit was created.
- [var component: AudioComponent](./component.md)
  The component found in the component description with which the audio unit was created.
- [var componentName: String?](./componentname.md)
  The audio unit’s component’s name.
- [var componentVersion: UInt32](./componentversion.md)
  The audio unit’s component’s version.
- [var audioUnitName: String?](./audiounitname.md)
  The audio unit’s name, derived from the component’s name.
- [var audioUnitShortName: String?](./audiounitshortname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/manufacturername)*