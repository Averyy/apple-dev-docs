# init(locale:identifier:version:)

**Framework**: Speech  
**Kind**: init

Constructs an empty data container.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
init(locale: Locale, identifier: String, version: String)
```

#### Discussion

The `SFCustomLanguageModelData` class accumulates language model training and custom vocabulary data, both associated with a specified locale. This initializer creates an object that initially holds no data.

## Parameters

- `locale`: The region and language of the training data (must match with the locale used to construct the   later)
- `identifier`: Used to uniquely identify the resulting language model on the device where it will be processed
- `version`: Used to distinguish different versions of the language model on the device where it will be processed

## See Also

- [convenience init(locale: Locale, identifier: String, version: String, builder: () -> any DataInsertable)](sfcustomlanguagemodeldata/init(locale:identifier:version:builder:).md)
  Constructs a data container using a builder
- [SFCustomLanguageModelData.DataInsertableBuilder](sfcustomlanguagemodeldata/datainsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/init(locale:identifier:version:))*