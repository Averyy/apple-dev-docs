# selectionColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

*Mac Catalyst*

```swift
@NSCopying
var selectionColor: UIColor? { get set }
```

*macOS*

```swift
@NSCopying
var selectionColor: NSColor? { get set }
```

*Mac Catalyst*

```objc
@property (copy, nullable) UIColor * selectionColor;
```

*macOS*

```objc
@property (copy, nullable) NSColor * selectionColor;
```

## See Also

### Handling selection
- [var selectedIndex: Int](./selectedindex.md)
- [var selectionMode: NSPickerTouchBarItem.SelectionMode](./selectionmode-swift.property.md)
- [NSPickerTouchBarItem.SelectionMode](./selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspickertouchbaritem/selectioncolor)*