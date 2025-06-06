# stringValue

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

The string is created by invoking [`description(withLocale:)`](nsnumber/description(withlocale:).md) where locale is `nil`.

## See Also

- [func description(withLocale: Any?) -> String](nsnumber/description(withlocale:).md)
  Returns a string that represents the contents of the number object for a given locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnumber/stringvalue)*