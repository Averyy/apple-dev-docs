# init(template:variables:)

**Framework**: Foundation  
**Kind**: init

Creates a new `URL` by expanding the RFC 6570 template and variables.

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
init?(template: URL.Template, variables: [URL.Template.VariableName : URL.Template.Value])
```

#### Discussion

This will fail if variable expansion does not produce a valid, well-formed URL.

All text will be converted to NFC (Unicode Normalization Form C) and UTF-8 before being percent-encoded if needed.

## Parameters

- `template`: The RFC 6570 template to be expanded.
- `variables`: Variables to expand in the template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/init(template:variables:))*