# contentBased

**Framework**: SwiftUI  
**Kind**: property

The writing direction following the language of the string that is laid out.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static let contentBased: Text.WritingDirectionStrategy
```

#### Discussion

The system may use different sources to determine the language of the string. This may include the characters used in the string, especially BiDi isolation markers, the language of the localization file the string was loaded from, or explicit annotations with the [`languageIdentifier`](https://developer.apple.com/documentation/Foundation/AttributeScopes/FoundationAttributes/languageIdentifier) attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/writingdirectionstrategy/contentbased)*