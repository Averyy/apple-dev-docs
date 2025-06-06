# init(_:_:_:)

**Framework**: Swiftdata  
**Kind**: init

Initializes a version struct with the provided components of a semantic version.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
init(_ major: Int, _ minor: Int, _ patch: Int)
```

#### Discussion

> **Note**: `major >= 0 && minor >= 0 && patch >= 0`.

## Parameters

- `major`: The major version number.
- `minor`: The minor version number.
- `patch`: The patch version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/version-swift.struct/init(_:_:_:))*