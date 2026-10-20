# IntentItem

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A type describing a value returned from a dynamic options provider, plus information about how to display it to users.

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
struct IntentItem<Value> where Value : _IntentValue
```

## Topics

### Initializers
- [init(Value)](./intentitem/init%28_%29.md)
  Initialize an `IntentItem` and use `displayRepresentation` from `value`
- [init(Value, title: LocalizedStringResource, subtitle: LocalizedStringResource?, image: DisplayRepresentation.Image?)](./intentitem/init%28_,title,subtitle,image%29.md)
  Creates an item with the specified value and visual attributes.
### Instance Properties
- [var description: DisplayRepresentation](./intentitem/description.md)
- [var value: Value](./intentitem/value.md)
### Enumerations
- [IntentItem.Builder](./intentitem/builder.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Items and collections
- [struct IntentItemCollection](./intentitemcollection.md)
  Return this object to provide an advanced list of options, optionally divided in sections.
- [struct IntentItemSection](./intentitemsection.md)
  An object you use to divide dynamic options into sections.
- [struct IntentCollectionSize](./intentcollectionsize.md)
- [struct IntentResponseStream](./intentresponsestream.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentitem)*