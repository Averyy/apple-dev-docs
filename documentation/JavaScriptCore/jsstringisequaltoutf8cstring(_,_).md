# JSStringIsEqualToUTF8CString(_:_:)

**Framework**: JavaScriptCore  
**Kind**: func  
**Role**: Function

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

```c
bool JSStringIsEqualToUTF8CString(JSStringRef a, const char *b);
```

#### Return Value

[`true`](../Swift/true.md) if the two strings match; otherwise, [`false`](../Swift/false.md).

## Parameters

- `a`: The [`JSStringRef`](./jsstringref.md) to test.
- `b`: The null-terminated UTF-8 string to test.

## See Also

### Comparing JavaScript Strings
- [func JSStringIsEqual(JSStringRef!, JSStringRef!) -> Bool](./jsstringisequal%28_,_%29.md)
  Tests whether two JavaScript strings match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsstringisequaltoutf8cstring(_:_:))*