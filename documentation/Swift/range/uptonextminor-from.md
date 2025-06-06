# upToNextMinor(from:)

**Framework**: Swift  
**Kind**: method

Returns a requirement for a version range, starting at the given minimum version and going up to the next minor version.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func upToNextMinor(from version: Version) -> Range<Bound> where Bound == Version
```

## Parameters

- `version`: The minimum version for the version range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/uptonextminor(from:))*