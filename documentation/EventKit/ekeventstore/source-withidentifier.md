# source(withIdentifier:)

**Framework**: EventKit  
**Kind**: method

Locates an event source with the specified identifier.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func source(withIdentifier identifier: String) -> EKSource?
```

#### Return Value

The source with the specified identifier, or `nil` if the source isn’t found.

## Parameters

- `identifier`: The source’s unique identifier.

## See Also

- [var sources: [EKSource]](ekeventstore/sources.md)
  An unordered array of objects that represent accounts that contain calendars.
- [var delegateSources: [EKSource]](ekeventstore/delegatesources.md)
  The event sources delegated to the person using your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/source(withidentifier:))*