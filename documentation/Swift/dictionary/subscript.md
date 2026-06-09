# subscript(_:_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the value at the given delimited key path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript(keyPath: String, delimiters: String) -> USDValue? { get set }
```

#### Overview

Reads return `nil` if no value is present at the path. Assigning a non-`nil` value sets it at the path, creating intermediate dictionaries as needed; assigning `nil` erases the value at the path.

## Parameters

- `keyPath`: A string of components separated by characters in `delimiters`.
- `delimiters`: The characters that separate path components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/subscript(_:_:))*