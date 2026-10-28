# contains(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the receiver contains the specified date.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func contains(_ date: Date) -> Bool
```

```objc
- (BOOL) containsDate:(NSDate *) date;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver contains `date`. Otherwise, [`false`](../../Swift/false.md).

## Parameters

- `date`: The date for which to test membership of the date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval/contains(_:))*