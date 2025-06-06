# init(platformString:)

**Framework**: System  
**Kind**: init

Creates a file path root by copying bytes from a null-terminated platform string. It is a precondition that a null byte indicates the end of the string. The absence of a null byte will trigger a runtime error.

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
init?(platformString: [CInterop.PlatformChar])
```

#### Discussion

Returns `nil` if `platformString` is empty or is not a root.

- Note It is a precondition that `platformString` must be null-terminated. The absence of a null byte will trigger a runtime error.

## Parameters

- `platformString`: A null-terminated platform string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/root-swift.struct/init(platformstring:)-3s0ol)*