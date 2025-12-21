# validate(url:)

**Framework**: Immersive Media Support  
**Kind**: method

Validates the AIVU file given its URL. It throws an error message with error details, if any.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func validate(url: URL) async throws -> Bool
```

#### Discussion

> **Note**: This function throws an exception with error details, if any.

## Parameters

- `url`: The url of an AIVU file to be validated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/aivuvalidator/validate(url:))*