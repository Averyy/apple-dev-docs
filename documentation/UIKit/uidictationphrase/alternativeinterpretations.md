# alternativeInterpretations

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of alternative textual interpretations of a dictated phrase.

**Availability**:
- iOS 5.1+
- iPadOS 5.1+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var alternativeInterpretations: [String]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSString *> * alternativeInterpretations;
```

## Discussion

If the system determines only one textual interpretation of a dictated phrase, the value of this property is `nil`. If there’s more than one interpretation, this property contains an array of strings, with the first being most likely interpretation and the last being the least likely.

## See Also

### Obtaining textual interpretations of spoken text
- [var text: String](./text.md)
  The most likely textual interpretation of a dictated phrase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidictationphrase/alternativeinterpretations)*