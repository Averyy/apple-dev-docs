# HMCharacteristicValueCurrentVisibilityState.alwaysShown

**Framework**: HomeKit  
**Kind**: case  
**Role**: Case

The media source is always displayed.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case alwaysShown
```

```c
HMCharacteristicValueCurrentVisibilityStateAlwaysShown
```

## Discussion

The media source can’t be hidden by writing to its Target Visibility State characteristic, even if one is included.

## See Also

### Visibility states
- [HMCharacteristicValueCurrentVisibilityState.connected](./connected.md)
  The media source is displayed since there’s a device connected to the input source.
- [HMCharacteristicValueCurrentVisibilityState.hidden](./hidden.md)
  The media source isn’t displayed.
- [HMCharacteristicValueCurrentVisibilityState.shown](./shown.md)
  The media source is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentvisibilitystate/alwaysshown)*