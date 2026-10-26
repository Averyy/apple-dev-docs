# optionsWithSpeed:

**Framework**: Symbols  
**Kind**: method  
**Role**: Type Method

A default set of effect options with a preferred speed multiplier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
+ (instancetype) optionsWithSpeed:(double) speed;
```

#### Return Value

A new instance of effect options with the preferred speed multiplier.

## Parameters

- `speed`: The preferred speed multiplier to play the effect with. The default multiplier is `1.0`. The function may clamp very large or small values.

## See Also

### Configuring effect speed
- [- optionsWithSpeed:](./optionswithspeed_-c.method.md)
  Creates a set of effect options with a preferred speed multiplier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboleffectoptions/optionswithspeed:-c.type.method)*