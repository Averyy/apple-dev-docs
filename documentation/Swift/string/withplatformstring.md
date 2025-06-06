# withPlatformString(_:)

**Framework**: Swift  
**Kind**: method

Calls the given closure with a pointer to the contents of the string, represented as a null-terminated platform string.

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
func withPlatformString<Result>(_ body: (UnsafePointer<CInterop.PlatformChar>) throws -> Result) rethrows -> Result
```

#### Return Value

The return value, if any, of the `body` closure parameter.

#### Discussion

The pointer passed as an argument to `body` is valid only during the execution of this method. Don’t try to store the pointer for later use.

## Parameters

- `body`: A closure with a pointer parameter   that points to a null-terminated platform string.   If   has a return value,   that value is also used as the return value for this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/withplatformstring(_:))*