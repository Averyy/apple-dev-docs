# IntentItemSection

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

An object you use to divide dynamic options into sections.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct IntentItemSection<Result> where Result : _IntentValue
```

## Overview

The system returns an `IntentItemSection` within an [`IntentItemCollection`](./intentitemcollection.md).

## Topics

### Initializers
- [init(LocalizedStringResource, items: [Result])](./intentitemsection/init%28_,items%29-2frw8.md)
- [init(LocalizedStringResource, items: [IntentItem<Result>])](./intentitemsection/init%28_,items%29-8p4y0.md)
- [init(LocalizedStringResource?, itemsBuilder: () -> [IntentItem<Result>])](./intentitemsection/init%28_,itemsbuilder%29.md)
- [init(LocalizedStringResource, subtitle: LocalizedStringResource?, image: DisplayRepresentation.Image?, itemsBuilder: () -> [IntentItem<Result>])](./intentitemsection/init%28_,subtitle,image,itemsbuilder%29.md)
- [init(items: [IntentItem<Result>])](./intentitemsection/init%28items%29.md)
- [init(title: LocalizedStringResource, items: [IntentItem<Result>])](./intentitemsection/init%28title,items%29.md)
### Instance Properties
- [var description: DisplayRepresentation?](./intentitemsection/description.md)
- [var items: [IntentItem<Result>]](./intentitemsection/items.md)
### Enumerations
- [IntentItemSection.Builder](./intentitemsection/builder.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Items and collections
- [struct IntentItem](./intentitem.md)
  A type describing a value returned from a dynamic options provider, plus information about how to display it to users.
- [struct IntentItemCollection](./intentitemcollection.md)
  Return this object to provide an advanced list of options, optionally divided in sections.
- [struct IntentCollectionSize](./intentcollectionsize.md)
- [struct IntentResponseStream](./intentresponsestream.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentitemsection)*