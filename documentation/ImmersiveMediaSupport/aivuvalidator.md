# AIVUValidator

**Framework**: Immersive Media Support  
**Kind**: struct

A type to validate existing AIVU files to ensure that they meet the minimum requirements for AIV.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct AIVUValidator
```

#### Overview

An AIVU is a standalone media file with the one or more video and audio tracks, and AIV required static and dynamic metadata.

## Topics

### Type Methods
- [static func validate(url: URL) async throws -> Bool](aivuvalidator/validate(url:).md)
  Validates the AIVU file given it’s URL. It throws an error message with error details, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/aivuvalidator)*