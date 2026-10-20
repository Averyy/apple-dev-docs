# init(title:)

**Framework**: EventKit  
**Kind**: init  
**Role**: Initializer

Creates a new structured location with the specified title.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(title: String)
```

```objc
+ (instancetype) locationWithTitle:(NSString *) title;
```

## Mentions

- [Setting an alarm](../setting-an-alarm.md)

#### Return Value

The structured location object.

## Parameters

- `title`: The title of the location.

## See Also

### Related Documentation
- [Calendar and Reminders Programming Guide](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009765)
### Creating Structured Locations
- [convenience init(mapItem: MKMapItem)](./init%28mapitem%29.md)
  Creates a new structured location with the specified map item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekstructuredlocation/init(title:))*