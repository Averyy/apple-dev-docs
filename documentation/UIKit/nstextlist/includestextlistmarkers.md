# includesTextListMarkers

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, readonly) BOOL includesTextListMarkers;
```

#### Overview

The default value is [`false`](../../Swift/false.md). When [`true`](../../Swift/true.md), TextKit includes text list markers in the text content.

## See Also

### Working with markers
- [var markerFormat: NSTextList.MarkerFormat](./markerformat-swift.property.md)
  Returns the marker format string used by the receiver.
- [NSTextList.MarkerFormat](./markerformat-swift.struct.md)
  Constants that describe marker symbols you can apply to list elements in text lists.
- [func marker(forItemNumber: Int) -> String](./marker%28foritemnumber%29.md)
  Returns the computed value for a specific ordinal position in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlist/includestextlistmarkers)*