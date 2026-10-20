# stringValue

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number object’s value expressed as a human-readable string.

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
var stringValue: String { get }
```

```objc
@property (copy, readonly) NSString * stringValue;
```

#### Discussion

The string is created by invoking [`description(withLocale:)`](./description%28withlocale%29.md) where locale is `nil`.

## See Also

### Retrieving String Representations
- [func description(withLocale: Any?) -> String](./description%28withlocale%29.md)
  Returns a string that represents the contents of the number object for a given locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnumber/stringvalue)*