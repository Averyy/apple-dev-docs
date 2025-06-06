# init(validating:)

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
init?(validating root: FilePath.Root)
```

#### Discussion

On Windows, creates a string from a path root, validating its contents as UTF-16 on Windows.

On Windows, if the contents of the path root isn’t a well-formed Unicode string, this initializer returns `nil`.

## Parameters

- `root`: The path root to be interpreted as   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(validating:)-6r2j9)*