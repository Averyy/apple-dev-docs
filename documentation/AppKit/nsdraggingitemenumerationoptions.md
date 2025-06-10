# NSDraggingItemEnumerationOptions

**Framework**: AppKit  
**Kind**: struct

A group of constants that specify options to use when enumerating dragging items.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct NSDraggingItemEnumerationOptions
```

## Topics

### Constants
- [static var concurrent: NSDraggingItemEnumerationOptions](nsdraggingitemenumerationoptions/concurrent.md)
  A constant that indicates the enumeration processes dragging items concurrently.
- [static var clearNonenumeratedImages: NSDraggingItemEnumerationOptions](nsdraggingitemenumerationoptions/clearnonenumeratedimages.md)
  A constant that indicates the enumeration clears the image components provider for all dragging items that don’t meet the classes and search options criteria.
### Initializers
- [init(rawValue: UInt)](nsdraggingitemenumerationoptions/init(rawvalue:).md)
  Creates a dragging enumeration option with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct NSDragOperation](nsdragoperation.md)
  A group of constants that represent which operations the dragging source can perform on dragging items.
- [enum NSSpringLoadingHighlight](nsspringloadinghighlight.md)
  A group of constants that indicate a highlighting style for your app’s user interface to display during a spring-loading operation.
- [enum NSDraggingFormation](nsdraggingformation.md)
  Constants that control the visual format of multiple dragging items.
- [enum NSDraggingContext](nsdraggingcontext.md)
  Constants that specify whether a drag terminates within or outside the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitemenumerationoptions)*