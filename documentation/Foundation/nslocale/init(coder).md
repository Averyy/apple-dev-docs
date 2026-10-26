# init(coder:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a locale initialized from data in the given unarchiver.

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
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

#### Return Value

The initialized locale.

## Parameters

- `coder`: The decoder to use during initialization.

## See Also

### Related Documentation
- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
### Initializing a Locale
- [init(localeIdentifier: String)](./init%28localeidentifier%29.md)
  Initializes a locale using a given locale identifier.
- [+ localeWithLocaleIdentifier:](./localewithlocaleidentifier_.md)
  Returns a locale initialized using the given locale identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/init(coder:))*