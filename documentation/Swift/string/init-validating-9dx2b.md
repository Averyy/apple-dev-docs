# init(validating:)

**Framework**: Swift  
**Kind**: init

Creates a string from a file path, validating its contents as UTF-8 on Unix and UTF-16 on Windows.

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
init?(validating path: FilePath)
```

#### Discussion

If the contents of the file path isn’t a well-formed Unicode string, this initializer returns `nil`.

## Parameters

- `path`: The file path to be interpreted as   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(validating:)-9dx2b)*