# init(fire:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a calendar event which fires based on the value of the supplied date components.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(fire fireDateComponents: DateComponents)
```

```objc
- (instancetype) initWithFireDateComponents:(NSDateComponents *) fireDateComponents;
```

## Return Value

An initialized calendar event.

## Parameters

- `fireDateComponents`: Date components that specify the time at which the event fires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcalendarevent/init(fire:))*