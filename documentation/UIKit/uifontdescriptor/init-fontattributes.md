# init(fontAttributes:)

**Framework**: UIKit  
**Kind**: init

Creates a font descriptor with the specified attributes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(fontAttributes attributes: [UIFontDescriptor.AttributeName : Any] = [:])
```

#### Return Value

The new font descriptor.

## Parameters

- `attributes`: The attributes for the new font descriptor. If  , the font descriptor’s attribute dictionary will be empty.

## See Also

- [convenience init()](uifontdescriptor/init.md)
  Creates a font descriptor.
- [init?(coder: NSCoder)](uifontdescriptor/init(coder:).md)
  Creates a font descriptor from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/init(fontattributes:))*