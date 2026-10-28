# isOpen

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the outline object is initially disclosed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isOpen: Bool { get set }
```

```objc
@property (nonatomic) BOOL isOpen;
```

## Discussion

Calling `isOpen` on an outline object that has no children always returns [`false`](../../Swift/false.md). Calling `isOpen` on the root outline object always returns [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfoutline/isopen)*