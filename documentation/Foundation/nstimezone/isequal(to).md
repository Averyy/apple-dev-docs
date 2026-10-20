# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the receiver has the same name and data as the specified time zone.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isEqual(to aTimeZone: TimeZone) -> Bool
```

```objc
- (BOOL) isEqualToTimeZone:(NSTimeZone *) aTimeZone;
```

#### Return Value

[`true`](../../Swift/true.md) if `aTimeZone` and the receiver have the same name and data, otherwise [`false`](../../Swift/false.md).

## Parameters

- `aTimeZone`: The time zone to compare with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/isequal(to:))*