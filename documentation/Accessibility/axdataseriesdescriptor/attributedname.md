# attributedName

**Framework**: Accessibility  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy) NSAttributedString * attributedName;
```

## Discussion

If you set the value of this property, the system uses this value instead of [`name`](./name.md).

## See Also

### Naming the series
- [var name: String?](./name.md)
  The name of the data series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdataseriesdescriptor/attributedname)*