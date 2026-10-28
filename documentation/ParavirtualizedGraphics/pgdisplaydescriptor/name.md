# name

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property

The display’s name as seen in the guest operating environment.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * name;
```

## Discussion

The default value is `Apple Virtual`. The framework truncates the name to 13 characters.

The device propagates the display name into the guest environment, so the name may be visible in the guest operating system’s user interface.

## See Also

### Specifying the Display Properties
- [var sizeInMillimeters: NSSize](./sizeinmillimeters.md)
  The size in millimeters of the virtual display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor/name)*