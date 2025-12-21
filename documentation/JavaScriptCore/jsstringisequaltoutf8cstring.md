# JSStringIsEqualToUTF8CString(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Tests whether a JavaScript string matches a null-terminated UTF-8 string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringIsEqualToUTF8CString(_ a: JSStringRef!, _ b: UnsafePointer<CChar>!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the two strings match; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `a`: The   to test.
- `b`: The null-terminated UTF-8 string to test.

## See Also

- [func JSStringIsEqual(JSStringRef!, JSStringRef!) -> Bool](jsstringisequal(_:_:).md)
  Tests whether two JavaScript strings match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringisequaltoutf8cstring(_:_:))*