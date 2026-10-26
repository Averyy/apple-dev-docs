# NSDragOperation

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A group of constants that represent which operations the dragging source can perform on dragging items.

**Availability**:
- macOS

## Declaration

```swift
struct NSDragOperation
```

```c
enum NSDragOperation : NSUInteger;
```

## Topics

### Constants
- [static var copy: NSDragOperation](./nsdragoperation/copy.md)
  A constant that indicates the drag can copy the data that the image represents.
- [static var link: NSDragOperation](./nsdragoperation/link.md)
  A constant that indicates the drag can share the data.
- [static var generic: NSDragOperation](./nsdragoperation/generic.md)
  A constant that indicates the destination can define the drag operation.
- [static var `private`: NSDragOperation](./nsdragoperation/private.md)
  A constant that indicates the source and destination negotiate the drag operation privately.
- [static var move: NSDragOperation](./nsdragoperation/move.md)
  A constant that indicates the drag can move the data.
- [static var delete: NSDragOperation](./nsdragoperation/delete.md)
  A constant that indicates the drag can delete the data.
- [static var every: NSDragOperation](./nsdragoperation/every.md)
  A constant that indicates that drag can perform all of the drag operations.
- [static var all: NSDragOperation](./nsdragoperation/all.md)
  Use [`every`](./nsdragoperation/every.md) instead.
- [static var all_Obsolete: NSDragOperation](./nsdragoperation/all_obsolete.md)
  The `NSDragOperationAll` constant is deprecated. Use [`every`](./nsdragoperation/every.md) instead.
- [NSDragOperationNone](./nsdragoperation/nsdragoperationnone.md)
  A constant that indicates that the drag cannot perform any operations.
### Initializers
- [init(rawValue: UInt)](./nsdragoperation/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

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
- [struct NSDraggingItemEnumerationOptions](./nsdraggingitemenumerationoptions.md)
  A group of constants that specify options to use when enumerating dragging items.
- [enum NSSpringLoadingHighlight](./nsspringloadinghighlight.md)
  A group of constants that indicate a highlighting style for your app’s user interface to display during a spring-loading operation.
- [enum NSDraggingFormation](./nsdraggingformation.md)
  Constants that control the visual format of multiple dragging items.
- [enum NSDraggingContext](./nsdraggingcontext.md)
  Constants that specify whether a drag terminates within or outside the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragoperation)*