# playbackMode

**Framework**: RealityKit

Metadata that controls animation idling until a behavior takes over.

#### Overview

Set the `playbackMode` metadata on the document’s , that is, the outermost container for scene description. For more information about setting stage metadata, see [`UsdStage`](https://developer.apple.comhttps://graphics.pixar.com/usd/docs/api/class_usd_stage.html) > Stage Metadata.

When an asset specifies playback metadata and a start animation, the animation plays automatically and loops until a trigger executes the `StartAnimationAction`. After the start animation completes, the asset’s behaviors ([`Preliminary_Behavior`](preliminary-behavior.md)) take control of the animation. If you don’t define a start animation for the asset, this property indicates whether an animation should restart after it finishes playing.

##### Declaration

```other
uniform token playbackMode = "loop" (       
    allowedTokens = ["none","loop"]
)
```

##### Playback Modes

##### Specify an Initial Idling Animation

The following metadata demonstrates `playbackMode` for an asset that defines a [`StartAnimationAction`](startanimationaction.md). This example sets [`playbackMode`](playbackmode.md) to `loop`, idling the animation in a perpetual replay until a trigger executes the start action.

```other
#usda 1.0
(
    endTimeCode = 300
    startTimeCode = 1
    timeCodesPerSecond = 30
    playbackMode = "loop"
    upAxis = "Y"
)

def Xform "AnimatedModel"
{
    def Xform "body"
    {
        double3 xformOp:translate.timeSamples = { ... }
        uniform token[] xformOpOrder = ["xformOp:translate"]
        ...
    }
    ...
}
```

## See Also

- [autoPlay](autoplay.md)
  Metadata that specifies whether an animation plays automatically on load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/playbackmode)*