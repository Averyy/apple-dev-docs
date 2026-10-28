# marker(forItemNumber:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the computed value for a specific ordinal position in the list.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func marker(forItemNumber itemNumber: Int) -> String
```

```objc
- (NSString *) markerForItemNumber:(NSInteger) itemNumber;
```

## Return Value

The computed maker value for `itemNumber`.

## Parameters

- `itemNumber`: The ordinal position in the list whose computed marker value is desired.

## See Also

### Working with markers
- [var markerFormat: NSTextList.MarkerFormat](./markerformat-swift.property.md)
  Returns the marker format string used by the receiver.
- [NSTextList.MarkerFormat](./markerformat-swift.struct.md)
  Constants that describe marker symbols you can apply to list elements in text lists.
- [class var includesTextListMarkers: Bool](./includestextlistmarkers.md)
  A Boolean value that indicates whether TextKit includes text list markers in the text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlist/marker(foritemnumber:))*