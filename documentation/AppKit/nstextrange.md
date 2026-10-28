# NSTextRange

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A class that represents a contiguous range between two locations inside document contents.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextRange
```

```objc
@interface NSTextRange : NSObject
```

## Overview

An `NSTextRange` consists of the starting and terminating locations. There the two basic properties: [`location`](./nstextrange/location.md) and [`endLocation`](./nstextrange/endlocation.md), respectively. The terminating [`location`](./nstextrange/location.md), [`endLocation`](./nstextrange/endlocation.md), is directly following the last location in the range. For example, a location contains a range if `(range.location <= location) && (location < range.endLocation)` is `true`.

## Topics

### Creating a text range
- [convenience init(location: any NSTextLocation)](./nstextrange/init%28location%29.md)
  Creates a new text range at the location you specify.
- [init?(location: any NSTextLocation, end: (any NSTextLocation)?)](./nstextrange/init%28location,end%29.md)
  Creates a new text range with the starting and ending locations you specify.
### Characteristics of the text range
- [var location: any NSTextLocation](./nstextrange/location.md)
  The starting location of the text range.
- [var endLocation: any NSTextLocation](./nstextrange/endlocation.md)
  The ending location of the text range.
- [var isEmpty: Bool](./nstextrange/isempty.md)
  Returns whether the text range is empty.
### Comparing text ranges
- [func intersection(NSTextRange) -> Self?](./nstextrange/intersection%28_%29.md)
  Returns the range, if any, where two text ranges intersect.
- [func intersects(NSTextRange) -> Bool](./nstextrange/intersects%28_%29.md)
  Determines if two ranges intersect.
- [func isEqual(to: NSTextRange) -> Bool](./nstextrange/isequal%28to%29.md)
  Compares two text ranges.
- [func union(NSTextRange) -> Self](./nstextrange/union%28_%29.md)
  Returns a new text range by forming the union with the text range you provide.
### Finding text within the text range
- [func contains(any NSTextLocation) -> Bool](./nstextrange/contains%28_%29-7hvi0.md)
  Determines if the text location you specify is in the current text range.
- [func contains(NSTextRange) -> Bool](./nstextrange/contains%28_%29-5j4y2.md)
  Determines if the text range you specify is in the current text range.
### Initializers
- [init?(location: any NSTextLocation, endLocation: (any NSTextLocation)?)](./nstextrange/init%28location,endlocation%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Location and selection
- [class NSTextSelection](./nstextselection.md)
  A class that represents a single logical selection context that corresponds to an insertion point.
- [class NSTextSelectionNavigation](./nstextselectionnavigation.md)
  An interface you use to expose methods for obtaining results from actions performed on text selections.
- [class NSTextSelectionManager](./nstextselectionmanager.md)
  An object that coordinates text selection behavior for custom text views.
- [protocol NSTextLocation](./nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextrange)*