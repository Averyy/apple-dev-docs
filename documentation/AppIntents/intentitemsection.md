# IntentItemSection

**Framework**: App Intents  
**Kind**: struct

An object you use to divide dynamic options into sections.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct IntentItemSection<Result> where Result : _IntentValue
```

#### Overview

The system returns an `IntentItemSection` within an [`IntentItemCollection`](intentitemcollection.md).

## Topics

### Initializers
- [init(LocalizedStringResource, items: [Result])](intentitemsection/init(_:items:)-2frw8.md)
- [init(LocalizedStringResource, items: [IntentItem<Result>])](intentitemsection/init(_:items:)-8p4y0.md)
- [init(LocalizedStringResource?, itemsBuilder: () -> [IntentItem<Result>])](intentitemsection/init(_:itemsbuilder:).md)
- [init(LocalizedStringResource, subtitle: LocalizedStringResource?, image: DisplayRepresentation.Image?, itemsBuilder: () -> [IntentItem<Result>])](intentitemsection/init(_:subtitle:image:itemsbuilder:).md)
- [init(items: [IntentItem<Result>])](intentitemsection/init(items:).md)
- [init(title: LocalizedStringResource, items: [IntentItem<Result>])](intentitemsection/init(title:items:).md)
### Instance Properties
- [var description: DisplayRepresentation?](intentitemsection/description.md)
- [var items: [IntentItem<Result>]](intentitemsection/items.md)
### Enumerations
- [IntentItemSection.Builder](intentitemsection/builder.md)

## See Also

- [struct IntentItem](intentitem.md)
  A type describing a value returned from a dynamic options provider, plus information about how to display it to users.
- [struct IntentItemCollection](intentitemcollection.md)
  Return this object to provide an advanced list of options, optionally divided in sections.
- [struct IntentCollectionSize](intentcollectionsize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentitemsection)*