# optionsWithRepeatCount:

**Framework**: Symbols  
**Kind**: method  
**Role**: Type Method

A default set of effect options with a preferred repeat count.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.2
- macOS 14.0+ - Deprecated in 27.2
- tvOS 17.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 10.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) optionsWithRepeatCount:(NSInteger) count;
```

#### Return Value

A new instance of effect options with the preferred repeat count.

## Parameters

- `count`: The preferred number of times to play the effect. The function may clamp very large or small values.

## See Also

### Configuring repeating effects
- [- optionsWithRepeating](./optionswithrepeating-c.method.md)
  A set of effect options that prefers to repeat indefinitely.
- [+ optionsWithRepeating](./optionswithrepeating-c.type.method.md)
  A default set of effect options that prefers to repeat indefinitely.
- [- optionsWithNonRepeating](./optionswithnonrepeating-c.method.md)
  A set of effect options that prefers to not repeat.
- [+ optionsWithNonRepeating](./optionswithnonrepeating-c.type.method.md)
  A default set of effect options that prefers to not repeat.
- [- optionsWithRepeatCount:](./optionswithrepeatcount_-c.method.md)
  Creates a set of effect options with a preferred repeat count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymboleffectoptions/optionswithrepeatcount:-c.type.method)*