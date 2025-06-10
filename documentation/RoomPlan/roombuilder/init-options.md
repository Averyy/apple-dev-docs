# init(options:)

**Framework**: RoomPlan  
**Kind**: init

Creates a room builder using the specified options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
init(options: RoomBuilder.ConfigurationOptions)
```

#### Discussion

Pass the [`beautifyObjects`](roombuilder/configurationoptions/beautifyobjects.md) option to enhance the look of the output for the captured room, or  (`[]`) to omit capture post-processing.

## Parameters

- `options`: An option set to customize the captured room.

## See Also

- [RoomBuilder.ConfigurationOptions](roombuilder/configurationoptions.md)
  Options that configure a room builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/roombuilder/init(options:))*