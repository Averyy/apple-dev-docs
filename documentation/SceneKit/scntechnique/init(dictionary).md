# init(dictionary:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a technique from a technique definition dictionary.,

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
init?(dictionary: [String : Any])
```

```objc
+ (SCNTechnique *) techniqueWithDictionary:(NSDictionary<NSString *,id> *) dictionary;
```

## Return Value

A new technique object.

## Discussion

See the class overview for details of a technique definition dictionary.

## Parameters

- `dictionary`: A dictionary defining the series of rendering passes that comprise the technique.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechnique/init(dictionary:))*