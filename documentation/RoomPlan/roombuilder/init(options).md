# init(options:)

**Framework**: RoomPlan  
**Kind**: init  
**Role**: Initializer

Creates a room builder using the specified options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
init(options: RoomBuilder.ConfigurationOptions)
```

#### Discussion

Pass the [`beautifyObjects`](./configurationoptions/beautifyobjects.md) option to enhance the look of the output for the captured room, or  (`[]`) to omit capture post-processing.

## Parameters

- `options`: An option set to customize the captured room.

## See Also

### Creating a room builder
- [RoomBuilder.ConfigurationOptions](./configurationoptions.md)
  Options that configure a room builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/init(options:))*