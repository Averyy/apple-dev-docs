# init(engine:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a single point in the environment from which sound emanates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(engine: PHASEEngine)
```

```objc
- (instancetype) initWithEngine:(PHASEEngine *) engine;
```

## Parameters

- `engine`: The object that controls this class’ associated audio output.

## See Also

### Creating a Source
- [init(engine: PHASEEngine, shapes: [PHASEShape])](./init%28engine,shapes%29.md)
  Creates a voluminous area in the environment from which sound emanates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesource/init(engine:))*