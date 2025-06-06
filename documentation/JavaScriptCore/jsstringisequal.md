# JSStringIsEqual(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func

Tests whether two JavaScript strings match.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func JSStringIsEqual(_ a: JSStringRef!, _ b: JSStringRef!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the two strings match; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `a`: The first   to test.
- `b`: The second   to test.

## See Also

- [func JSStringIsEqualToUTF8CString(JSStringRef!, UnsafePointer<CChar>!) -> Bool](jsstringisequaltoutf8cstring(_:_:).md)
  Tests whether a JavaScript string matches a null-terminated UTF-8 string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringisequal(_:_:))*