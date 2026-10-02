# includesTextListMarkers

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether TextKit includes text list markers in the text content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class var includesTextListMarkers: Bool { get }
```

#### Overview

The default value is [`false`](https://developer.apple.com/documentation/swift/false). When [`true`](https://developer.apple.com/documentation/swift/true), TextKit includes text list markers in the text content.

## See Also

- [var markerFormat: NSTextList.MarkerFormat](nstextlist/markerformat-swift.property.md)
  Returns the marker format string used by the receiver.
- [NSTextList.MarkerFormat](nstextlist/markerformat-swift.struct.md)
  Constants that describe marker symbols you can apply to list elements in text lists.
- [func marker(forItemNumber: Int) -> String](nstextlist/marker(foritemnumber:).md)
  Returns the computed value for a specific ordinal position in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlist/includestextlistmarkers)*