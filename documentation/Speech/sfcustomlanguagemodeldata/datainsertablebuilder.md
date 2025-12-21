# SFCustomLanguageModelData.DataInsertableBuilder

**Framework**: Speech  
**Kind**: struct

A custom parameter attribute that constructs custom language model data from closures.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
@resultBuilder
struct DataInsertableBuilder
```

#### Overview

The `SFCustomLanguageModelData` class provides two methods for accumulating data: manually constructing `PhraseCount` and `CustomPronunciation` objects and providing them using the `insert` methods defined below, or by using the result builder DSL upon initialization. This type supports the latter.

## Topics

### Result builder methods
- [static func buildArray([any DataInsertable]) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildarray(_:).md)
  Enables support for `for..in` loops.
- [static func buildBlock(any DataInsertable...) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildblock(_:).md)
  Combines statement blocks into a single product.
- [static func buildEither(first: any DataInsertable) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildeither(first:).md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildEither(second: any DataInsertable) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildeither(second:).md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildOptional((any DataInsertable)?) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildoptional(_:).md)
  Enables support for `if` statements that do not have an `else` clause.

## See Also

- [convenience init(locale: Locale, identifier: String, version: String, builder: () -> any DataInsertable)](sfcustomlanguagemodeldata/init(locale:identifier:version:builder:).md)
  Constructs a data container using a builder
- [init(locale: Locale, identifier: String, version: String)](sfcustomlanguagemodeldata/init(locale:identifier:version:).md)
  Constructs an empty data container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/datainsertablebuilder)*