# dataDetectorMatches(_:options:)

**Framework**: Swift  
**Kind**: method

Searches for known data types in a string or a substring.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func dataDetectorMatches(_ types: DataDetector.MatchType = .all, options: DataDetector.Options = DataDetector.Options()) -> some AsyncSequence<DataDetector.Match, Never>
```

#### Return Value

An [`AsyncSequence`](asyncsequence.md) of `DataDetector/Match` objects that match the provided string.

#### Discussion

DataDetection only searches for known data types in natural language text. There’s no guarantee that the framework can find a particular matching string in the  data, especially in ambiguous cases. The scanner expects an input string in a person’s language and region, if supported. However, the framework may consider some additional languages and regions. Don’t use this functionality to validate form inputs such as email addresses, postal addresses, URLs, and so on.

The following example functions show how to scan for email addresses, links, calendar events, and measurements in strings.

```swift
import DataDetection

/// Returns the number of emails from example.com in the provided string.
func countExampleEmails(text: String) async -> Int {
    var countExampleEmails: Int = 0
    for await match in text.dataDetectorMatches([.emailAddress]) {
        if case let .emailAddress(email) = match.details {
            if email.emailAddress.hasSuffix("@example.com") {
                countExampleEmails += 1
            }
        }
    }
    return countExampleEmails
}

/// Returns an attributed string that highlights links, calendar events, and measurements the data detection finds in the provided string.
func underline(text: String) async -> AttributedString {
    var attributedText = AttributedString(text)
    for await match in text.dataDetectorMatches([.link, .calendarEvent, .measurement]) {
        if let range = match.range, let attributedRange = Range(range, in: attributedText) {
            var attributes = AttributeContainer ()
            switch match.preferredHighlightStyle {
            case .hidden:
                continue
            case .url:
                attributes.underlineColor = .linkColor
            default:
                let color = attributedText[attributedRange].foregroundColor ?? .textColor
                attributes.underlineColor = color.withAlphaComponent(0.26)
            }
            attributedText[attributedRange].mergeAttributes(attributes, mergePolicy: .keepNew)
        }
    }
    return attributedText
}
```

> **Note**: This API can be resource intensive. While usually fast with short strings, its performance can vary greatly depending on the input size and content. Always avoid blocking the main thread or any critical task on this call.

## Parameters

- `options`: The   to customize the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/datadetectormatches(_:options:))*