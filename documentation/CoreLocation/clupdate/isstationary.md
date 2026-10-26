# isStationary

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device is stationary.

**Availability**:
- iOS 17.0+ - Deprecated in 17.0
- iPadOS 17.0+ - Deprecated in 17.0
- Mac Catalyst 17.0+ - Deprecated in 17.0
- macOS 14.0+ - Deprecated in 14.0
- tvOS 17.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 10.0+ - Deprecated in 10.0

## Declaration

```objc
@property (readonly) BOOL isStationary;
```

#### Discussion

Updates may stop flowing temporarily for several reasons including if the app is no longer authorized to receive location updates or if its location becomes unknown. If Core Location stops delivering updates because the device is stationary, then it sets `isStationary` to [`true`](../../Swift/true.md); otherwise, it’s [`false`](../../Swift/false.md).

If `isStationary` is [`true`](../../Swift/true.md), then the framework can suspend updates until the person starts moving, or their location becomes unknown.

## See Also

### Update properties
- [location](./location.md)
  A person’s location, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clupdate/isstationary)*