# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new layout fragment with the coder you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: A coder that conforms to [`NSCoder`](../../Foundation/nscoder.md).

## See Also

### Creating a layout fragment
- [init(textElement: NSTextElement, range: NSTextRange?)](./init%28textelement,range%29.md)
  Create a new layout fragment using the provided text element and range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/init(coder:))*