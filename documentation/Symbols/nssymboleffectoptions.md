# NSSymbolEffectOptions

**Framework**: Symbols  
**Kind**: class  
**Role**: Class

Options that configure how effects apply to symbol-based images.

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
@interface NSSymbolEffectOptions : NSObject
```

## Topics

### Accessing effect options
- [+ options](./nssymboleffectoptions/options.md)
  The default set of effect options.
### Configuring repeating effects
- [- optionsWithRepeating](./nssymboleffectoptions/optionswithrepeating-c.method.md)
  A set of effect options that prefers to repeat indefinitely.
- [+ optionsWithRepeating](./nssymboleffectoptions/optionswithrepeating-c.type.method.md)
  A default set of effect options that prefers to repeat indefinitely.
- [- optionsWithNonRepeating](./nssymboleffectoptions/optionswithnonrepeating-c.method.md)
  A set of effect options that prefers to not repeat.
- [+ optionsWithNonRepeating](./nssymboleffectoptions/optionswithnonrepeating-c.type.method.md)
  A default set of effect options that prefers to not repeat.
- [- optionsWithRepeatCount:](./nssymboleffectoptions/optionswithrepeatcount_-c.method.md)
  Creates a set of effect options with a preferred repeat count.
- [+ optionsWithRepeatCount:](./nssymboleffectoptions/optionswithrepeatcount_-c.type.method.md)
  A default set of effect options with a preferred repeat count.
### Configuring effect speed
- [- optionsWithSpeed:](./nssymboleffectoptions/optionswithspeed_-c.method.md)
  Creates a set of effect options with a preferred speed multiplier.
- [+ optionsWithSpeed:](./nssymboleffectoptions/optionswithspeed_-c.type.method.md)
  A default set of effect options with a preferred speed multiplier.
### Instance Methods
- [- optionsWithRepeatBehavior:](./nssymboleffectoptions/optionswithrepeatbehavior_-c.method.md)
  Return a copy of the options setting a preferred repeat behavior.
### Type Methods
- [+ optionsWithRepeatBehavior:](./nssymboleffectoptions/optionswithrepeatbehavior_-c.type.method.md)
  Convenience initializer setting a preferred repeat behavior.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Symbol effect options
- [NSSymbolEffectOptionsRepeatBehavior](./nssymboleffectoptionsrepeatbehavior.md)
  The behavior of repetition to use when a symbol effect is animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboleffectoptions)*