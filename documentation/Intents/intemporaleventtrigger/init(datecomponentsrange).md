# init(dateComponentsRange:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the event trigger with the specified date information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(dateComponentsRange: INDateComponentsRange)
```

```objc
- (instancetype) initWithDateComponentsRange:(INDateComponentsRange *) dateComponentsRange;
```

#### Return Value

An initialized event trigger object or `nil` if the object could not be created.

## Parameters

- `dateComponentsRange`: The time range during which the event is triggered. To trigger an event at a specific time, specify the same value for both the start and end dates of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtrigger/init(datecomponentsrange:))*