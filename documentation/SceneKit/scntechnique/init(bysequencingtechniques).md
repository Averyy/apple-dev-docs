# init(bySequencingTechniques:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a new rendering technique that combines a series of techniques.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
init?(bySequencingTechniques techniques: [SCNTechnique])
```

```objc
+ (SCNTechnique *) techniqueBySequencingTechniques:(NSArray<SCNTechnique *> *) techniques;
```

## Return Value

A new technique object.

## Discussion

The new technique applies the effects of the techniques in the order specified in the `techniques` array. Each output of a technique in the array becomes an input to the next technique in the array.

## Parameters

- `techniques`: An array of [`SCNTechnique`](../scntechnique.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechnique/init(bysequencingtechniques:))*