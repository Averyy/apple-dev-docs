# CTParagraphStyleCreateCopy(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates an immutable copy of a paragraph style.

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
func CTParagraphStyleCreateCopy(_ paragraphStyle: CTParagraphStyle) -> CTParagraphStyle
```

```c
extern CTParagraphStyleRefCTParagraphStyleCreateCopy(CTParagraphStyleRef paragraphStyle);
```

## Return Value

A valid reference to an immutable CTParagraphStyle object that is a copy of the one passed into `paragraphStyle`, If the `paragraphStyle` reference is valid; otherwise `NULL`, if any error occurred, including being supplied with an invalid reference.

## Parameters

- `paragraphStyle`: The style to copy. This parameter may not be `NULL`.

## See Also

### Creating Paragraph Styles
- [func CTParagraphStyleCreate(UnsafePointer<CTParagraphStyleSetting>?, Int) -> CTParagraphStyle](./ctparagraphstylecreate%28_,_%29.md)
  Creates an immutable paragraph style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctparagraphstylecreatecopy(_:))*