# CTParagraphStyleCreate(_:_:)

**Framework**: Core Text  
**Kind**: func

Creates an immutable paragraph style.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTParagraphStyleCreate(_ settings: UnsafePointer<CTParagraphStyleSetting>?, _ settingCount: Int) -> CTParagraphStyle
```

#### Return Value

A valid reference to an immutable CTParagraphStyle object, If the paragraph style creation was successful; otherwise, `NULL`.

#### Discussion

Using this function is the easiest and most efficient way to create a paragraph style. Paragraph styles should be kept immutable for totally lock-free operation. If an invalid paragraph style setting specifier is passed into the `settings` parameter, nothing bad will happen, but you will be unable to query for this value. The reason is to allow backward compatibility with style setting specifiers that may be introduced in future versions.

## Parameters

- `settings`: The settings with which to preload the paragraph style. If you want to specify the default set of settings, set this parameter to  .
- `settingCount`: The number of settings that you have specified in the   parameter. This must be greater than or equal to  .

## See Also

- [func CTParagraphStyleCreateCopy(CTParagraphStyle) -> CTParagraphStyle](ctparagraphstylecreatecopy(_:).md)
  Creates an immutable copy of a paragraph style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstylecreate(_:_:))*