# primaryLanguage

**Framework**: UIKit  
**Kind**: property

The primary language for a custom keyboard.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var primaryLanguage: String? { get set }
```

#### Discussion

A BCP 47 language identifier, such as `en-US`. If specified, this value supersedes the `PrimaryLanguage` key in a custom keyboard’s `Info.plist` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/primarylanguage)*