# init(engine:shapes:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a voluminous area in the environment from which sound emanates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(engine: PHASEEngine, shapes: [PHASEShape])
```

```objc
- (instancetype) initWithEngine:(PHASEEngine *) engine shapes:(NSArray<PHASEShape *> *) shapes;
```

## Parameters

- `engine`: The object that controls this class’ associated audio output.
- `shapes`: A list of volumes that emanate sound.

## See Also

### Creating a Source
- [init(engine: PHASEEngine)](./init%28engine%29.md)
  Creates a single point in the environment from which sound emanates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesource/init(engine:shapes:))*