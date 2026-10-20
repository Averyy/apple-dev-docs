# alternativeStrings

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of alternative possible interpretations that the user might select.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var alternativeStrings: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * alternativeStrings;
```

#### Discussion

The text system presents the alternative strings via a user interface similar to that used for spelling correction alternatives.

## See Also

### Storing Alternative Text Strings
- [var primaryString: String](./primarystring.md)
  The text that was initially chosen as the input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextalternatives/alternativestrings)*