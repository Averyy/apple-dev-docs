# dateComponentsRange

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The triggering time range for an event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var dateComponentsRange: INDateComponentsRange { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INDateComponentsRange * dateComponentsRange;
```

*macOS*

```objc
@property (atomic, copy, readonly) INDateComponentsRange * dateComponentsRange;
```

## Discussion

This property is set automatically at initialization time and can’t be changed later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtrigger/datecomponentsrange)*