# marker(forItemNumber:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the computed value for a specific ordinal position in the list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func marker(forItemNumber itemNumber: Int) -> String
```

```objc
- (NSString *) markerForItemNumber:(NSInteger) itemNumber;
```

## Return Value

The computed maker value for `itemNum`.

## Parameters

- `itemNumber`: The ordinal position in the list whose computed marker value is desired.

## See Also

### Working with markers
- [var markerFormat: NSTextList.MarkerFormat](./markerformat-swift.property.md)
  Returns the marker format string used by the receiver.
- [NSTextList.MarkerFormat](./markerformat-swift.struct.md)
  Constants that describe marker symbols you can apply to list elements in text lists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlist/marker(foritemnumber:))*