# NINearbyObjectDistanceNotAvailable

**Framework**: Nearby Interaction  
**Kind**: var  
**Role**: Global Variable

An object that indicates the peer’s distance is unavailable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```c
extern float NINearbyObjectDistanceNotAvailable;
```

## Mentions

- [Initiating and maintaining a session](./initiating-and-maintaining-a-session.md)

#### Discussion

The framework sets [`distance`](./ninearbyobject/distance-9atp7.md) to the value of this property if it’s unable to acquire distance at any given time.

## See Also

### Acquring relative distance
- [distance](./ninearbyobject/distance-9atp7.md)
  The distance from the user’s device to the peer device in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobjectdistancenotavailable)*