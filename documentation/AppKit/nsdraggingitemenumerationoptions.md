# NSDraggingItemEnumerationOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A group of constants that specify options to use when enumerating dragging items.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct NSDraggingItemEnumerationOptions
```

```c
enum NSDraggingItemEnumerationOptions : NSUInteger;
```

## Topics

### Constants
- [static var concurrent: NSDraggingItemEnumerationOptions](./nsdraggingitemenumerationoptions/concurrent.md)
  A constant that indicates the enumeration processes dragging items concurrently.
- [static var clearNonenumeratedImages: NSDraggingItemEnumerationOptions](./nsdraggingitemenumerationoptions/clearnonenumeratedimages.md)
  A constant that indicates the enumeration clears the image components provider for all dragging items that don’t meet the classes and search options criteria.
### Initializers
- [init(rawValue: UInt)](./nsdraggingitemenumerationoptions/init%28rawvalue%29.md)
  Creates a dragging enumeration option with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [struct NSDragOperation](./nsdragoperation.md)
  A group of constants that represent which operations the dragging source can perform on dragging items.
- [enum NSSpringLoadingHighlight](./nsspringloadinghighlight.md)
  A group of constants that indicate a highlighting style for your app’s user interface to display during a spring-loading operation.
- [enum NSDraggingFormation](./nsdraggingformation.md)
  Constants that control the visual format of multiple dragging items.
- [enum NSDraggingContext](./nsdraggingcontext.md)
  Constants that specify whether a drag terminates within or outside the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingitemenumerationoptions)*