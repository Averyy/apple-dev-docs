# attributedName

**Framework**: Accessibility  
**Kind**: property

An attributed version of the data series name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@NSCopying
var attributedName: NSAttributedString { get set }
```

#### Discussion

If you set the value of this property, the system uses this value instead of [`name`](axdataseriesdescriptor/name.md).

## See Also

- [var name: String?](axdataseriesdescriptor/name.md)
  The name of the data series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdataseriesdescriptor/attributedname)*