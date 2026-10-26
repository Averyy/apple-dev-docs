# init(start:end:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a relevance provider with the specified start and end dates.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(start startDate: Date, end endDate: Date?)
```

```objc
- (instancetype) initWithStartDate:(NSDate *) startDate endDate:(NSDate *) endDate;
```

#### Return Value

A newly initialized date relevance provider.

## Parameters

- `startDate`: A relevant start date for the provider.
- `endDate`: An optional relevant end date for the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indaterelevanceprovider/init(start:end:))*