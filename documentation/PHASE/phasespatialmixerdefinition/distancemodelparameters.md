# distanceModelParameters

**Framework**: PHASE  
**Kind**: property

An effect that changes sound as it carries over a distance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var distanceModelParameters: PHASEDistanceModelParameters? { get set }
```

#### Discussion

Similar to a Doppler effect, this property changes how an audio source sounds as its distance between the listener increases or decreases in 3D space. The available options are:

- **[`PHASEGeometricSpreadingDistanceModelParameters`](phasegeometricspreadingdistancemodelparameters.md)**: Create a realistic effect by dissipating certain frequency ranges of the audio spectrum differently with distance.
- **[`PHASEEnvelopeDistanceModelParameters`](phaseenvelopedistancemodelparameters.md)**: Take full control of the sound’s volume by graphing its loudness using points and curves over the distance.

##### Programmatically Check Sound Dissipation

After setting a value for this property, you can move a looping sound source to tweak the effect to your app’s particular requirements. The following code programmaticaly moves a looping source away from the listener along the z-axis:

**Swift**:

```swift
spatialSamplerNode.playbackType = PHASEPlaybackType.looping
// ... 
var sourceTransform: PHASETransform3D = origin
sourceTransform.columns.3.z -= 6.0
while (true) {
    var posToSet: PHASETransform3D = source.transform
    posToSet.columns.3.z -= 0.05
    if (posToSet.columns.3.z < -20.0)
    {
        posToSet.columns.3.z = -6.0;
    }
    source.transform = posToSet
    usleep(20000) // 20 ms
    print("z =", source.transform.columns.3.z);
}     
```

**Objective-C**:

```objc
spatialSamplerNode.playbackType = PHASEPlaybackTypeLooping;
// ...
PHASETransform3D sourceTransform = origin;
sourceTransform.columns[3].z -= 6.f;
while (1) {
    PHASETransform3D posToSet = _source.transform;
    posToSet.columns[3].z -= .05f;
    if (posToSet.columns[3].z < -20.f)
    {
        posToSet.columns[3].z = -6.f;
    }
    _source.transform = posToSet;
    [NSThread sleepForTimeInterval:.02f]; // 20 ms
    NSLog(@"z = %f", _source.transform.columns[3].z);
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialmixerdefinition/distancemodelparameters)*