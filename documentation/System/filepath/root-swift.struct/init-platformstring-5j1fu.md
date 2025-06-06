# init(platformString:)

**Framework**: System  
**Kind**: init

Creates a file path root by copying bytes from a null-terminated platform string.

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
init?(platformString: UnsafePointer<CInterop.PlatformChar>)
```

#### Discussion

Returns `nil` if `platformString` is empty or is not a root.

## Parameters

- `platformString`: A pointer to a null-terminated platform   string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/root-swift.struct/init(platformstring:)-5j1fu)*