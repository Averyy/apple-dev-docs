# AUNodeRenderCallback

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

A callback used to provide input to an audio unit.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AUNodeRenderCallback
```

```c
struct AUNodeRenderCallback;
```

#### Overview

Used to contain information when a callback is used to provide input to the specific node’s specified input.

## Topics

### Initializers
- [init()](./aunoderendercallback/init%28%29.md)
- [init(destNode: AUNode, destInputNumber: AudioUnitElement, cback: AURenderCallbackStruct)](./aunoderendercallback/init%28destnode,destinputnumber,cback%29.md)
### Instance Properties
- [var cback: AURenderCallbackStruct](./aunoderendercallback/cback.md)
- [var destInputNumber: AudioUnitElement](./aunoderendercallback/destinputnumber.md)
- [var destNode: AUNode](./aunoderendercallback/destnode.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Data Types
- [struct AudioUnitNodeConnection](./audiounitnodeconnection.md)
  A connection between two node objects in an audio processing graph.
- [typealias AUGraph](./augraph.md)
  An opaque type representing an audio processing graph.
- [typealias AUNode](./aunode.md)
  A member of an audio processing graph, associated with an audio unit.
- [struct AUNodeInteraction](./aunodeinteraction.md)
  Describes the interaction between two node objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aunoderendercallback)*