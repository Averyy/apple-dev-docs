# init(bySequencingTechniques:)

**Framework**: SceneKit  
**Kind**: init

Creates a new rendering technique that combines a series of techniques.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init?(bySequencingTechniques techniques: [SCNTechnique])
```

#### Return Value

A new technique object.

#### Discussion

The new technique applies the effects of the techniques in the order specified in the `techniques` array. Each output of a technique in the array becomes an input to the next technique in the array.

## Parameters

- `techniques`: An array of   objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechnique/init(bysequencingtechniques:))*