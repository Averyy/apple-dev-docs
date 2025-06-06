# $effectiveMaximumMovieRating

**Framework**: ManagedSettings  
**Kind**: property

The movie rating constraint that is active on this device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var $effectiveMaximumMovieRating: Published<Int>.Publisher { get }
```

## Mentions

- [Confirming the Effective TV and Movie Ratings](readingmedia.md)

#### Discussion

An authorized app can use the Family Controls framework to apply a [`maximumMovieRating`](mediasettings/maximummovierating-swift.property.md) to the device. If no `maximumMovieRating` settings are active, then the value of this property is the default value of  [`maximumMovieRating`](mediasettings/maximummovierating-swift.type.property.md). The system publishes changes dynamically.

## See Also

- [var objectWillChange: ObservableObjectPublisher](managedsettingsstore/objectwillchange.md)
- [var $effectiveMaximumTVShowRating: Published<Int>.Publisher](managedsettingsstore/$effectivemaximumtvshowrating.md)
  The television show rating constraint that is active on this device.
- [ManagedSettingsStore.ObjectWillChangePublisher](managedsettingsstore/objectwillchangepublisher.md)
  The type of publisher that emits before the object has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/managedsettingsstore/$effectivemaximummovierating)*