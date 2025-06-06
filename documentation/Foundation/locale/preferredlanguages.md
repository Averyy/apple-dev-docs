# preferredLanguages

**Framework**: Foundation  
**Kind**: property

A list of the user’s preferred languages.

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
static var preferredLanguages: [String] { get }
```

#### Discussion

> **Note**:  [`Bundle`](bundle.md) is responsible for determining the language that your application will run in, based on the result of this API and combined with the languages your application supports.

 [`Bundle`](bundle.md) is responsible for determining the language that your application will run in, based on the result of this API and combined with the languages your application supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/preferredlanguages)*