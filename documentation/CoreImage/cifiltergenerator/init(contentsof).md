# init(contentsOf:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initializes a filter generator object with the contents of a filter generator file.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(contentsOf aURL: URL)
```

```objc
- (id) initWithContentsOfURL:(NSURL *) aURL;
```

#### Return Value

The initialized [`CIFilterGenerator`](../cifiltergenerator.md) object. Returns `nil` if the file can’t be read.

## Parameters

- `aURL`: The location of a filter generator file.

## See Also

### Related Documentation
- [+ filterGeneratorWithContentsOfURL:](./filtergeneratorwithcontentsofurl_.md)
  Creates and returns a filter generator object and initializes it with the contents of a filter generator file.
- [+ filterGenerator](./filtergenerator.md)
  Creates and returns an empty filter generator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/init(contentsof:))*