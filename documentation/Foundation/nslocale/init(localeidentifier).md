# init(localeIdentifier:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a locale using a given locale identifier.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(localeIdentifier string: String)
```

```objc
- (instancetype) initWithLocaleIdentifier:(NSString *) string;
```

#### Return Value

The initialized locale.

#### Discussion

This method is the designated initializer for this class.

## Parameters

- `string`: The identifier for the new locale.

## See Also

### Related Documentation
- [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)
- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
### Initializing a Locale
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns a locale initialized from data in the given unarchiver.
- [+ localeWithLocaleIdentifier:](./localewithlocaleidentifier_.md)
  Returns a locale initialized using the given locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/init(localeidentifier:))*