# PHASEConeDirectivityModelParameters

**Framework**: PHASE  
**Kind**: class

An object that directs sound in a cone-shaped curve that extends from a sound source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEConeDirectivityModelParameters
```

#### Overview

This class determines that a particular frequency range in the audio spectrum emits sound in an area defined by a mathematical cone. PHASE refers to each frequency segment along the audio spectrum as a *subband*. This class contains an array of `subbands` that each direct sound in a unique cone shape. The framework outputs a blend of a frequency’s adjacent subbands for all frequencies that lie outside of those specified in the `subbands` array.

##### Emit Sound in the Shape of a Cone

The following code defines a cone directivity model with two subbands. The first subband emits sound in a narrow region and the second subband outputs sound in a wider region.

**Swift**:

```swift
let simpleCone = PHASEConeDirectivityModelParameters()

let coneSegment1 = PHASEConeDirectivityModelSubbandParameters()
coneSegment1.frequency = 500.0
coneSegment1.innerAngle = 60.0
coneSegment1.outerAngle = 80.0
coneSegment1.outerGain = 0.5

let coneSegment2 = PHASEConeDirectivityModelSubbandParameters()
coneSegment2.frequency = 5000.0
coneSegment2.innerAngle = 30.0
coneSegment2.outerAngle = 40.0
coneSegment2.outerGain = 0.3

simpleCone.subbands.add(coneSegment1)
simpleCone.subbands.add(coneSegment2)

spatialMixer.listenerDirectivityModelParameters = simpleCone
```

**Objective-C**:

```objc
PHASEConeDirectivityModelParameters* simpleCone = 
    [[PHASEConeDirectivityModelParameters alloc] init];

PHASEConeDirectivityModelSubbandParameters* coneSegment1 = 
    [[PHASEConeDirectivityModelSubbandParameters alloc] init];
coneSegment1.frequency = 5000.f;
coneSegment1.innerAngle = 30.f;
coneSegment1.outerAngle = 40.f;
coneSegment1.outerGain = .3f;

PHASEConeDirectivityModelSubbandParameters* coneSegment2 = 
    [[PHASEConeDirectivityModelSubbandParameters alloc] init];
coneSegment2.frequency = 500.f;
coneSegment2.innerAngle = 60.f;
coneSegment2.outerAngle = 80.f;
coneSegment2.outerGain = .5f;

[simpleCone.subbands addObject:coneSegment1];
[simpleCone.subbands addObject:coneSegment2];

spatialMixer.listenerDirectivityModelParameters = simpleCone;
```

![An illustration of two different cone directivity configurations. On the left, a narrow cone contains a slightly narrower cone. A callout extends from the outer cone’s point that indicates its angle is 40 degrees. A callout extends from the inner cone’s point that indicates its angle is 30 degrees. On the right, a wide cone rests inside a slightly wider cone. A callout extends from the outer cone’s point that indicates its angle is 80 degrees. A callout extends from the inner cone’s point that indicates its angle is 60 degrees. In both configurations, a sphere rests on the cone’s point to indicate the user’s position in relation to the cone. ](/images/com.apple.phase/media-3887365@2x.png)

## Topics

### Creating the Cone Directivity Model Parameters
- [init(subbandParameters: [PHASEConeDirectivityModelSubbandParameters])](phaseconedirectivitymodelparameters/init(subbandparameters:).md)
  Creates an object that directs sound in a cone-shaped curve that extends from a sound source.
### Defining Subbands
- [var subbandParameters: [PHASEConeDirectivityModelSubbandParameters]](phaseconedirectivitymodelparameters/subbandparameters.md)
  An array of frequencies that describe varying sound emission across the spectrum.

## Relationships

### Inherits From
- [PHASEDirectivityModelParameters](phasedirectivitymodelparameters.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class PHASECardioidDirectivityModelParameters](phasecardioiddirectivitymodelparameters.md)
  An object that directs sound in a heart-shaped curve surrounding a sound source.
- [class PHASECardioidDirectivityModelSubbandParameters](phasecardioiddirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a heart.
- [class PHASEConeDirectivityModelSubbandParameters](phaseconedirectivitymodelsubbandparameters.md)
  A data set that projects sound of a certain frequency outward in the shape of a cone.
- [class PHASEDirectivityModelParameters](phasedirectivitymodelparameters.md)
  A base class for objects that direct sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseconedirectivitymodelparameters)*