# init(rawValue:)

**Framework**: System  
**Kind**: init

Creates a strongly-typed file type from the raw C `mode_t`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(rawValue: CInterop.Mode)
```

#### Discussion

> **Note**: This initializer stores the `rawValue` directly and **does not** mask the value with `S_IFMT`. If the supplied `rawValue` contains bits outside of the `S_IFMT` mask, the resulting `FileType` will not compare equal to constants like `.directory` and `.symbolicLink`, which may be unexpected. If you’re unsure whether the `mode_t` contains bits outside of `S_IFMT`, you can use `FileMode(rawValue:)` instead to get a strongly-typed `FileMode`, then call `.type` to get the properly masked `FileType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filetype/init(rawvalue:))*