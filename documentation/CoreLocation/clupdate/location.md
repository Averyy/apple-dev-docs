# location

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A person’s location, if available.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (nonatomic, readonly) CLLocation * location;
```

## Discussion

If the location isn’t available, the value is `nil`.

## See Also

### Update properties
- [isStationary](./isstationary.md)
  A Boolean value that indicates whether the device is stationary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clupdate/location)*