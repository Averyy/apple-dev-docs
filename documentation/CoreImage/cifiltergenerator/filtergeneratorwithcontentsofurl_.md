# filterGeneratorWithContentsOfURL:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates and returns a filter generator object and initializes it with the contents of a filter generator file.

**Availability**:
- macOS 10.5+

## Declaration

```objc
+ (CIFilterGenerator *) filterGeneratorWithContentsOfURL:(NSURL *) aURL;
```

#### Return Value

A [`CIFilterGenerator`](../cifiltergenerator.md) object;  returns `nil` if the file can’t be read.

## Parameters

- `aURL`: The location of a filter generator file.

## See Also

### Creating Filter Generator Objects
- [+ filterGenerator](./filtergenerator.md)
  Creates and returns an empty filter generator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/filtergeneratorwithcontentsofurl:)*