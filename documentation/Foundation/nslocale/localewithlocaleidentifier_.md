# localeWithLocaleIdentifier:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a locale initialized using the given locale identifier.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) localeWithLocaleIdentifier:(NSString *) ident;
```

## Return Value

The initialized locale.

## Parameters

- `ident`: The identifier for the new locale.

## See Also

### Initializing a Locale
- [init(localeIdentifier: String)](./init%28localeidentifier%29.md)
  Initializes a locale using a given locale identifier.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns a locale initialized from data in the given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/localewithlocaleidentifier:)*