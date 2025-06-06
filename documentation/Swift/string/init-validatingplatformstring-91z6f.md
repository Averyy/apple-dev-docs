# init(validatingPlatformString:)

**Framework**: Swift  
**Kind**: init

Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.

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
init?(validatingPlatformString platformString: [CInterop.PlatformChar])
```

#### Discussion

- Note It is a precondition that `platformString` must be null-terminated. The absence of a null byte will trigger a runtime error.

If the contents of the platform string isn’t well-formed Unicode, this initializer returns `nil`.

## Parameters

- `platformString`: The null-terminated platform string to be   interpreted as  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(validatingplatformstring:)-91z6f)*