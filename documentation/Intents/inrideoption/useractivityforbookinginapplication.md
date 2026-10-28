# userActivityForBookingInApplication

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user activity object that you can use to launch the app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var userActivityForBookingInApplication: NSUserActivity? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readwrite, nullable) NSUserActivity * userActivityForBookingInApplication;
```

*macOS*

```objc
@property (atomic, strong, readwrite, nullable) NSUserActivity * userActivityForBookingInApplication;
```

## Mentions

- [Generating a List of Ride Options](../../SiriKit/generating-a-list-of-ride-options.md)

## Discussion

Set the value of this property to `nil` when you want to allow SiriKit to complete the booking of rides in its interface. When the value of this property is `nil`, Siri and Maps display ride option information directly from their respective interfaces.

Assigning a user activity object to this property causes SiriKit to launch your app so that you can complete the booking instead. You might ask SiriKit to launch your app when you want to convey additional information to the user. For example, when a pickup or drop-off location involves an airport, you might want SiriKit to launch your app so that you can ask for terminal and flight information.

The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/useractivityforbookinginapplication)*