# init(primaryString:alternativeStrings:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes an `NSTextAlternatives` instance.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(primaryString: String, alternativeStrings: [String])
```

```objc
- (instancetype) initWithPrimaryString:(NSString *) primaryString alternativeStrings:(NSArray<NSString *> *) alternativeStrings;
```

#### Return Value

An initialized `NSTextAlternatives` instance.

## Parameters

- `primaryString`: The string that is initially chosen as the input string.
- `alternativeStrings`: An array of alternative possible interpretations that the user might select.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextalternatives/init(primarystring:alternativestrings:))*