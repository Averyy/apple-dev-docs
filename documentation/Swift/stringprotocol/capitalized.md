# capitalized

**Framework**: Swift  
**Kind**: property

A copy of the string with each word changed to its corresponding capitalized spelling.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var capitalized: String { get }
```

#### Discussion

This property performs the canonical (non-localized) mapping. It is suitable for programming operations that require stable results not depending on the current locale.

A capitalized string is a string with the first character in each word changed to its corresponding uppercase value, and all remaining characters set to their corresponding lowercase values. A “word” is any sequence of characters delimited by spaces, tabs, or line terminators. Some common word delimiting punctuation isn’t considered, so this property may not generally produce the desired results for multiword strings. See the `getLineStart(_:end:contentsEnd:for:)` method for additional information.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/capitalized)*