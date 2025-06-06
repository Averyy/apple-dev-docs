# init(decoding:)

**Framework**: Swift  
**Kind**: init

On Unix, creates the string `"/"`

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(decoding root: FilePath.Root)
```

#### Discussion

On Windows, creates a string by interpreting the path root’s content as UTF-16.

If the content of the path root isn’t a well-formed Unicode string, this initializer replaces invalid bytes with U+FFFD. This means that on Windows, conversion to a string and back to a path root might result in a value that’s different from the original path root.

## Parameters

- `root`: The path root to be interpreted as   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(decoding:)-364r2)*